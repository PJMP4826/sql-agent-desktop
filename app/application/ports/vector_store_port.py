from typing import List
from abc import ABC, abstractmethod
from app.domain.entities.document import Document
from llama_index.core.vector_stores.types import BasePydanticVectorStore


class VectorStorePort(ABC):

    @property
    @abstractmethod
    def get_vector_store(self) -> BasePydanticVectorStore:
        pass

    # @abstractmethod
    # def add_documents(self, documents: List[Document]) -> List[str]:
    #     pass

    # buscar documentos
    @abstractmethod
    def query(self, query_text: str, top_k: int = 5) -> List[Document]:
        pass

    @abstractmethod
    def delete_documents(self, ids: List[str]) -> bool:
        pass

    @abstractmethod
    def delete_collection(self) -> bool:
        pass

    @abstractmethod
    def get_collection_count(self) -> int:
        pass
