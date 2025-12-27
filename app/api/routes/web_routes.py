import sys
from fastapi import APIRouter
from fastapi.responses import FileResponse
from pathlib import Path


router = APIRouter()


def get_static_path() -> Path:
    if getattr(sys, 'frozen', False):
        return Path(sys._MEIPASS) 
    return Path(__file__).parent.parent.parent.parent

@router.get("/")
def server_index():
    basic_path = get_static_path()

    INDEX_FILE_PATH = basic_path / "index.html"
    # print(INDEX_FILE_PATH)
    if not INDEX_FILE_PATH.exists():
        raise FileNotFoundError(f"No hya index.html en {INDEX_FILE_PATH}")
    return FileResponse(INDEX_FILE_PATH)


@router.get("/{full_path:path}")
def serve_spa(full_path: str):
    base_path = get_static_path()
    INDEX_FILE_PATH = base_path / "index.html"
    if not INDEX_FILE_PATH.exists():
        raise FileNotFoundError(f"No hya index.html en {INDEX_FILE_PATH}")
    return FileResponse(INDEX_FILE_PATH)
