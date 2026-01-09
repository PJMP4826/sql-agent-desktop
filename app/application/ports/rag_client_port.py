from abc import ABC, abstractmethod

class RAG_CLIENT_PORT(ABC):
    @abstractmethod
    def chat(self, question: str) -> str:
        raise NotImplementedError

    @abstractmethod
    async def async_chat(self, question: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def query(self, query: str) -> str:
        raise NotImplementedError

    @abstractmethod
    async def async_query(self, query: str) -> str:
        raise NotImplementedError
