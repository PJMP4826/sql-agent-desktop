from typing import List
from abc import ABC, abstractmethod
from app.domain.entities.document import Document


class VectorStorePort(ABC):
    @abstractmethod
    def add_documents(self, documents: List[Document]) -> List[str]:
        pass

    # buscar documentos
    @abstractmethod
    def query(self, query_text: str, top_k: int = 5) -> List[Document]:
        pass

    @abstractmethod
    def delete_documents(self, ids: List[str]):
        pass

    @abstractmethod
    def delete_collection(self) -> bool:
        pass

    @abstractmethod
    def get_collection_count(self) -> int:
        pass
