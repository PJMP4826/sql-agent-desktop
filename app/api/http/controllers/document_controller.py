from typing import List
from fastapi import UploadFile
from fastapi.responses import JSONResponse
from app.domain.repositories.document_repository import DocumentRepository


class DocumentController:
    def __init__(self, repository: DocumentRepository) -> None:
        self.repository = repository

    async def upload_handle_files(self, files: List[UploadFile]):
        savedFile = await self.repository.guardarDocumento(files)
        if savedFile:
            return JSONResponse(content={"guardado": True}, status_code=200)
        else:
            return JSONResponse(content={"guardado": False}, status_code=500)
