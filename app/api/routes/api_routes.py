from fastapi import APIRouter
from fastapi import UploadFile, File
from typing import List
from app.api.http.controllers.document_controller import upload_handle_files

router = APIRouter(prefix="/api")


@router.post("/uploads/files")
async def upload_file(file: UploadFile = File(...)):
    return await upload_handle_files([file])

@router.post("/uploads/multiples/files")
async def upload_files(files: List[UploadFile] = File(...)):
    return await upload_handle_files(files)
