import os
import json
from typing import List
from pathlib import Path
from fastapi import UploadFile


class DocumentRepository:
    def __init__(self, path: str = "./docs"):
        self.path = Path(path)
        self.documentos_dir = self.path / "files"

    def crearDirectoriosNecesarios(self):
        self.documentos_dir.mkdir(parents=True, exist_ok=True)
        return self.documentos_dir.resolve()

    async def guardarDocumento(self, files: List[UploadFile]) -> bool:
        try:
            save_path = self.crearDirectoriosNecesarios()
            for file in files:
                contenido = await file.read()
                file_path = save_path / file.filename
                with open(file_path, "wb") as f:
                    f.write(contenido)
            return True
        except FileNotFoundError:
            return False


# if __name__ == "__main__":
#     try:
#         rep = DocumentRepository()
#         rep.crearDirectoriosNecesarios()
#         print("Creado exitosamente")
#     except Exception as e:
#         print(f"Error faltal {e}")
