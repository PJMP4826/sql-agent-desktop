from typing import List, Any
from abc import ABC, abstractmethod


class VectorStorePort(ABC):
    @abstractmethod
    def store_documents(self, documents: List[Any]) -> None:
        pass

    @abstractmethod
    def query(self, query_text: str, top_k: int = 5) -> List[Any]:
        pass

    @abstractmethod
    def get_collection_count(self) -> int:
        pass
