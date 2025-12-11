from typing import Optional, Any
from llama_index.core import VectorStoreIndex
from llama_index.core import StorageContext
from app.application.ports.vector_store_port import VectorStorePort
from app.domain.services.document_manager import DocumentManager
from app.shared.domain_exceptions import DomainException
from config.settings import Settings
from llama_index.core.indices.base import BaseIndex
from llama_index.core.base.base_query_engine import BaseQueryEngine
from llama_index.core.schema import Document
from llama_index.core.chat_engine.types import ChatMode, BaseChatEngine


class RagService:
    def __init__(self, vector_store: VectorStorePort) -> None:
        self.system_prompt_path: Optional[str] = None
        self.vector_store = vector_store
        self.document_manager = DocumentManager(self.vector_store)

        self._index: Optional[BaseIndex[Any]] = None
        self._chat_query: Optional[BaseChatEngine] = None
        self._query_engine: Optional[BaseQueryEngine] = None


    #def _create_index(self) -> VectorStoreIndex:


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
        return self._create_index_from_documents()

    def add_document(self, document: Document):
        try:
            self.index.insert(document=document)
        except Exception as e:
            raise DomainException(
                "Error al agregar documento", details={"error": str(e)}
            )

    @property
    def chat_engine(self) -> BaseChatEngine:
        return self.index.as_chat_engine(
            chat_mode=ChatMode.CONDENSE_PLUS_CONTEXT,
            system_prompt=(self.system_prompt_path),
            verbose=False,
        )

    @property
    def query_engine(self):
        return self.index.as_query_engine()

    def chat(self, user_input: str) -> str:
        return str(self.chat_engine.chat(user_input))

    # recordatorio: implementar def chat() en el agent
