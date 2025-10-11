from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from entities.Document import Document

class DocumentRepositoryInterface(ABC):
    @classmethod
    @abstractmethod
    async def guardarDocumento(self,documen: Document, file_content: bytes = None) -> str:
        pass

    async def eliminarDocumento(self, doc_id: str) -> bool:
        pass