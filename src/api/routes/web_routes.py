from fastapi import FastAPI
from fastapi import APIRouter
from fastapi.responses import FileResponse
from pathlib import Path


router = APIRouter()


@router.get("/")
def server_index():
    INDEX_FILE_PATH = Path(__file__).parent.parent.parent.parent / "index.html"
    # print(INDEX_FILE_PATH)
    if not INDEX_FILE_PATH.exists():
        raise FileNotFoundError(f"No hya index.html en {INDEX_FILE_PATH}")
    return FileResponse(INDEX_FILE_PATH)


@router.get("/{full_path:path}")
def serve_spa(full_path: str):
    INDEX_FILE_PATH = Path(__file__).parent.parent.parent.parent / "index.html"
    if not INDEX_FILE_PATH.exists():
        raise FileNotFoundError(f"No hya index.html en {INDEX_FILE_PATH}")
    return FileResponse(INDEX_FILE_PATH)
