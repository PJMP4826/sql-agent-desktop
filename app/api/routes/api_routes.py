from fastapi import APIRouter
from fastapi import UploadFile, File
from typing import List
from app.config.dependencies import get_document_controller

router = APIRouter(prefix="/api")

controller = get_document_controller()

@router.post("/uploads/files")
async def upload_file(file: UploadFile = File(...)):
    return await controller.upload_handle_files([file])

@router.post("/uploads/multiples/files")
async def upload_files(files: List[UploadFile] = File(...)):
    return await controller.upload_handle_files(files)
