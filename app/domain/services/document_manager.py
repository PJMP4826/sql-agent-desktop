import os
from pathlib import Path
from typing import List, Optional
from llama_index.core import (
    SimpleDirectoryReader,
    Document as LlamaDocument,
)
from app.application.ports.vector_store_port import VectorStorePort
from app.shared.domain_exceptions import DomainException
from llama_index.core.schema import Document
from typing import Any


class DocumentManager:

    ALLOWED_EXTENSIONS = [".pdf", ".txt", ".md", ".docx", ".doc", ".csv"]
    
    def __init__(self, vector_store: VectorStorePort) -> None:
        self.vector_store = vector_store
        self.file_extensions = [".pdf", ".txt", ".md", ".docx", ".doc"]

    def validate_file(self, file_path: str) -> dict[str, Any]:
        file_path_obj = Path(file_path)

        if not file_path_obj.exists():
            raise DomainException(
                "Archivo no encontrado",
                details={"file_path": file_path}
            )

        #verificar que sea archivo
        if not file_path_obj.is_file():
            raise DomainException(
                "Path no es un archivo",
                details={"file_path": file_path}
            )

        extension: str = file_path_obj.suffix.lower()

        #verificar extension
        if extension not in self.ALLOWED_EXTENSIONS:
            raise DomainException(
                "Tipo de archivo no soportado",
                details={
                    "file_path": file_path,
                    "extension": extension,
                    "allowed_extensions": self.ALLOWED_EXTENSIONS
                }
            )
        
        return {
            "valid": True,
            "file_path": str(file_path_obj),
            "file_name": file_path_obj.name,
            "extension": extension,
        }

    def validate_files(self, files_paths: List[str]) -> dict[str, List[dict[str, str]] | int]:
        valid_files: List[dict[str, str]] = []
        invalid_files: List[dict[str, str]] = []
        
        for file_path in files_paths:
            try:

                validation = self.validate_file(file_path)

                valid_files.append(validation)
            except DomainException as e:
                invalid_files.append({
                    "file_path": file_path,
                    "error": str(e)
                })
        
        return {
            "valid_files": valid_files,
            "invalid_files": invalid_files,
            "valid_files_count": len(valid_files),
            "invalid_files_count": len(invalid_files)
        }
            
    def load_documents_from_directory(
        self, path: str, file_extensions: Optional[List[str]] = None
    ) -> List[LlamaDocument]:

        if file_extensions is None:
            file_extensions = self.file_extensions

        try:

            is_directory: bool = os.path.isdir(path)
            is_file: bool = os.path.isfile(path)

            if not is_directory and not is_file:
                raise ValueError(
                    "La rura proporcionada no es un directorio ni archivo valido"
                )
            
            reader_params = {"required_exts": file_extensions}
            if is_directory:
                reader_params = ["input_dir"] = path

            if is_file:
                reader_params = ["input_files"] = [path]


            reader = SimpleDirectoryReader(
                **reader_params
            )

            documents: List[Document] = reader.load_data()

            return documents
        except Exception as e:
            raise DomainException(
                "Error al cargar los archivos",
                details={"path": path, "error": str(e)},
            )
        
        
    def add_documents(self, file_paths: List[str]) -> dict:
        try:
            valid_files: List[str] = []
            invalid_files: List[str] = []

            for file_path in file_paths:
                file_path_obj = Path(file_path)

                if not file_path_obj.exists():
                    invalid_files.append(file_path)

                valid_files.append(file_path)

            if not valid_files:
                raise DomainException(
                    "No hay archivos validos para indexar",
                    details={"invalid_files": invalid_files}
                )
            
            documents = SimpleDirectoryReader(
                input_files=valid_files
            ).load_data()

            #for doc in documents:


        except Exception as e:
            raise DomainException(
                "Error al indexar archivos",
                details={"file_count": len(file_paths), "error": str(e)},
            )

    