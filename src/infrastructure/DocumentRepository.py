import os
import json
import asyncio
import aiofiles
from datetime import datetime
from typing import List, Optional, Dict, Any
from pathlib import Path
from core.entities.Document import Document


class DocumentRepository:
    def __init__(self, path: str = "./docs"):
        self.path = Path(path)
        self.documentos_dir = self.path / "files"
        self.metadata_dir = self.path / "metadata"

    def crearDirectoriosNecesarios(self):
        self.documentos_dir.mkdir(parents=True, exist_ok=True)
        self.metadata_dir.mkdir(parents=True, exist_ok=True)

    async def guardarDocumento(
        self, document: Document, fileContent: bytes = None
    ) -> str:
        try:
            
            document.updated_at = datetime.utcnow()

           
            content_to_save = (
                fileContent if fileContent else document.content.encode("utf-8")
            )
            document_path = self._get_document_path(document.id)

            async with aiofiles.open(document_path, "wb") as f:
                await f.write(content_to_save)

           
            document.file_path = str(document_path)
            document.size_bytes = len(content_to_save)

            
            metadata = {
                "id": document.id,
                "title": document.title,
                "file_type": document.file_type,
                "size_bytes": document.size_bytes,
                "metadata": document.metadata,
                "tags": document.tags,
                "created_at": document.created_at.isoformat(),
                "updated_at": document.updated_at.isoformat(),
                "file_path": document.file_path,
            }

            metadata_path = self._get_metadata_path(document.id)
            async with aiofiles.open(metadata_path, "w", encoding="utf-8") as f:
                await f.write(json.dumps(metadata, indent=2, ensure_ascii=False))

            return document.id

        except Exception as e:
            raise Exception(f"Error saving document {document.id}: {str(e)}")


# if __name__ == "__main__":
#     try:
#         rep = DocumentRepository()
#         rep.crearDirectoriosNecesarios()
#         print("Creado exitosamente")
#     except Exception as e:
#         print(f"Error faltal {e}")
