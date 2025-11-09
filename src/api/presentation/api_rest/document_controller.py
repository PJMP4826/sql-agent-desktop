from typing import List
from fastapi import UploadFile
from fastapi.responses import JSONResponse
from src.infrastructure.document_repository import DocumentRepository


async def upload_handle_files(files: List[UploadFile]):
    repository = DocumentRepository()
    savedFile = await repository.guardarDocumento(files)
    if savedFile:
        return JSONResponse(content={"guardado": True}, status_code=200)
    else:
        return JSONResponse(content={"guardado": False}, status_code=500)
