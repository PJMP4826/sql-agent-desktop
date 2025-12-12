from typing import Optional, Any
from llama_index.core import VectorStoreIndex
from llama_index.core import StorageContext
from app.application.ports.vector_store_port import VectorStorePort
from app.domain.services.document_manager import DocumentManager
from app.shared.domain_exceptions import DomainException
from config.settings import Settings
from llama_index.core.indices.base import BaseIndex
from llama_index.core.base.base_query_engine import BaseQueryEngine
from pathlib import Path
from llama_index.core.chat_engine.types import ChatMode, BaseChatEngine

from app.application.ports.llm_port import LLMPort


class RagService:
    def __init__(
        self,
        vector_store: VectorStorePort,
        llm_client: LLMPort,
        system_prompt_path: Optional[str],
        auto_index_on_empty: bool = False,
    ) -> None:
        self.system_prompt_path: Optional[str] = system_prompt_path
        self.vector_store = vector_store
        self.settings = Settings()  # type: ignore

        self.document_manager = DocumentManager()

        self._index: Optional[BaseIndex[Any]] = None
        self._chat_engine: Optional[BaseChatEngine] = None
        self._query_engine: Optional[BaseQueryEngine] = None

        self.llm_client = llm_client

    def _is_vectore_store_empty(self) -> bool:
        try:
            return self.vector_store.get_collection_count() == 0
        except Exception:
            return False

    def _create_storage_context(self) -> StorageContext:
        self.storage_context = StorageContext.from_defaults(
            vector_store=self.vector_store.get_vector_store
        )

    def _create_index(self):
        try:
            if not self._is_vectore_store_empty():
                index: VectorStoreIndex = VectorStoreIndex(
                    nodes=[], storage_context=self.storage_context
                )

            index: VectorStoreIndex = VectorStoreIndex.from_vector_store(
                vector_store=self.vector_store.get_vector_store,
                embed_model=self.llm_client.get_embed_model(),
            )

            return index
        except Exception as e:
            raise DomainException(
                "Error creando vector index", details={"error": str(e)}
            )

    def _create_index_from_documents(self) -> VectorStoreIndex:
        try:
            storage_context = StorageContext.from_defaults(
                vector_store=self.vector_store.get_vector_store
            )

            index = VectorStoreIndex.from_documents(
                self.document_manager, storage_context=storage_context
            )

            return index

        except Exception as e:
            raise DomainException(
                "Error al crear index de Vectore Store", details={"error": str(e)}
            )

    @property
    def index(self):
        if self._index is None:
            self._index = self._create_index()
        return self._index

    @property
    def chat_engine(self) -> BaseChatEngine:
        if self._chat_engine is None:
            self._chat_engine = self.index.as_chat_engine(
                chat_mode=ChatMode.CONDENSE_PLUS_CONTEXT,
                system_prompt=self.system_prompt_path,
                verbose=False,
            )
        return self._chat_engine

    @property
    def query_engine(self) -> BaseQueryEngine:
        """Lazy loading del query engine con cache"""
        if self._query_engine is None:
            self._query_engine = self.index.as_query_engine()
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
                documents, storage_context=storage_context, show_progress=True
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
            raise DomainException(
                "Error indexing directory",
                details={"directory": directory, "error": str(e)},
            )

    def add_document(self, file_path: str) -> dict[str, Any]:
        try:

            documents = self.document_manager.load_document(file_path)

            inserted_count = 0

            for doc in documents:
                self.index.insert(document=doc)
                insert_count += 1

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

            self.vector_store.get_collection_count()

            self.refresh_all()

            result = self.index_directory()

            return result

        except Exception as e:
            raise DomainException(
                "Error re-indexing documentos", details={"error": str(e)}
            )

    def chat(self, user_input: str) -> str:
        return str(self.chat_engine.chat(user_input))

    # recordatorio: implementar def chat() en el agent
