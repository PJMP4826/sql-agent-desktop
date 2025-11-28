from abc import ABC, abstractmethod


# herramienta que un agente puede usar
# como http, db, rag
class Tool(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @property
    def description(self) -> str:
        return ""

    @abstractmethod
    async def run(self, **kwargs) -> any:
        raise NotImplementedError
