import logging
from typing import Optional, Any
from llama_index.core import VectorStoreIndex
from llama_index.core import StorageContext
from app.application.ports.vector_store_port import VectorStorePort
from app.domain.services.document_manager import DocumentManager
from app.shared.domain_exceptions import DomainException
from app.config.settings import Settings
from llama_index.core.indices.base import BaseIndex
from llama_index.core.base.base_query_engine import BaseQueryEngine
from pathlib import Path
from llama_index.core.chat_engine.types import ChatMode, BaseChatEngine

from app.application.ports.llm_port import LLMPort

logger = logging.getLogger(__name__)



class RagService:
    def __init__(
        self,
        vector_store: VectorStorePort,
        llm_client: LLMPort,
        system_prompt: Optional[str],
        auto_index_on_empty: bool = False,
    ) -> None:
        self.system_prompt: Optional[str] = system_prompt
        #print("System Prompt: ", self.system_prompt)
        self.vector_store = vector_store
        self.settings = Settings()  # type: ignore

        self.document_manager = DocumentManager()

        self._index: Optional[BaseIndex[Any]] = None
        self._chat_engine: Optional[BaseChatEngine] = None
        self._query_engine: Optional[BaseQueryEngine] = None

        self.llm_client = llm_client

        if auto_index_on_empty and self._is_vectore_store_empty():
                try:
                    self.index_directory()
                except Exception as e:
                    logger.error(f"Auto-indexing failed: {e}")

    def _is_vectore_store_empty(self) -> bool:
        try:
            count:int = self.vector_store.get_collection_count()

            return count == 0
        except Exception:
            return False

    def _create_storage_context(self) -> StorageContext:
        return StorageContext.from_defaults(
            vector_store=self.vector_store.get_vector_store
        )

    def _create_index(self) -> VectorStoreIndex:
        try:

            storage_context = self._create_storage_context()

            if self._is_vectore_store_empty():
                return VectorStoreIndex(
                    nodes=[], 
                    storage_context=storage_context,
                    embed_model=self.llm_client.get_embed_model()
                )

            # el vector store no es empty
            index: VectorStoreIndex = VectorStoreIndex.from_vector_store(  # type: ignore
                vector_store=self.vector_store.get_vector_store,
                embed_model=self.llm_client.get_embed_model(),
            )

            return index
        except Exception as e:
            raise DomainException(
                "Error creando vector index", details={"error": str(e)}
            )

    @property
    def index(self):
        if self._index is None:
            self._index = self._create_index()
        return self._index

    @property
    def chat_engine(self) -> BaseChatEngine:
        if self._chat_engine is None:

            system_prompt = self.system_prompt

            self._chat_engine = self.index.as_chat_engine(  # type: ignore
                llm=self.llm_client.get_llm_model(),
                chat_mode=ChatMode.BEST,
                system_prompt=system_prompt,
                verbose=False,
            )
        return self._chat_engine

    @property
    def query_engine(self) -> BaseQueryEngine:
        """Lazy loading del query engine con cache"""
        if self._query_engine is None:
            self._query_engine = self.index.as_query_engine( # type: ignore
                llm=self.llm_client.get_llm_model()
            )  # type: ignore
        return self._query_engine

    def refresh_engines(self):
        """Refrescar engines despues de cambios en el indice"""
        self._chat_engine = None
        self._query_engine = None

    # refrescar todo (indice y engines)
    def refresh_all(self):
        self._index = None
        self._chat_engine = None
        self._query_engine = None

    def index_directory(
        self,
        directory: Optional[str] = None,
        recursive: bool = True,
    ) -> dict[str, Any]:

        try:
            directory = directory or self.settings.docs_path

            documents = self.document_manager.load_documents_from_directory(
                directory_path=directory, recursive=recursive
            )

            if not documents:
                return {
                    "directory": directory,
                    "documents_loaded": 0,
                    "documents_indexed": 0,
                    "total_in_store": self.vector_store.get_collection_count(),
                }

            storage_context = self._create_storage_context()

            new_index = VectorStoreIndex.from_documents(
                documents,
                storage_context=storage_context,
                embed_model=self.llm_client.get_embed_model(),
                show_progress=True,
            )

            self._index = new_index
            self.refresh_engines()

            return {
                "directory": directory,
                "documents_loaded": len(documents),
                "total_in_store": self.vector_store.get_collection_count(),
            }

        except DomainException:
            raise
        except Exception as e:
            print(str(e))
            raise DomainException(
                "Error indexing directory",
                details={"directory": directory, "error": str(e)},
            )

    def add_document(self, file_path: str) -> dict[str, Any]:
        try:

            documents = self.document_manager.load_document(file_path)

            inserted_count: int = 0

            for doc in documents:
                self.index.insert(document=doc)
                inserted_count += 1

            self.refresh_engines()

            return {
                "file_path": file_path,
                "filename": Path(file_path).name,
                "documents_inserted": inserted_count,
                "total_in_store": self.vector_store.get_collection_count(),
            }

        except Exception as e:
            raise DomainException(
                "Error al agregar documento",
                details={"file_path": file_path, "error": str(e)},
            )

    def reindex_all(self) -> dict[str, Any]:
        """
        limpiar y re-indexar todo desde el directorio base.
        """
        try:

            self.vector_store.delete_collection()

            self.refresh_all()

            result = self.index_directory()

            return result

        except Exception as e:
            raise DomainException(
                "Error re-indexing documentos", details={"error": str(e)}
            )

    def query(self, user_input: str) -> str:
        try:
            response = self.query_engine.query(user_input)

            return str(response)
        except Exception as e:
            raise DomainException(
                "Error en query, usando query_engine",
                details={"question": user_input, "error": str(e)},
            )

    # consultar pero usando el contexto de la conversation
    def chat(self, user_input: str) -> str:
        try:
            response = self.chat_engine.chat(user_input)

            return str(response)
        except Exception as e:
            raise DomainException(
                "Error en chat, usando chat_engine",
                details={"question": user_input, "error": str(e)},
            )
