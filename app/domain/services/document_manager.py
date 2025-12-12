from pathlib import Path
from typing import List, Optional
from llama_index.core import (
    SimpleDirectoryReader,
    Document as LlamaDocument,
)
from app.shared.domain_exceptions import DomainException
from llama_index.core.schema import Document
from typing import Any


class DocumentManager:

    ALLOWED_EXTENSIONS = [".pdf", ".txt", ".md", ".docx", ".doc", ".csv"]

    def __init__(self):
        self.file_extensions = [".pdf", ".txt", ".md", ".docx", ".doc"]

    def validate_file(self, file_path: str) -> dict[str, Any]:
        file_path_obj = Path(file_path)

        if not file_path_obj.exists():
            raise DomainException(
                "Archivo no encontrado", details={"file_path": file_path}
            )

        # verificar que sea archivo
        if not file_path_obj.is_file():
            raise DomainException(
                "Path no es un archivo", details={"file_path": file_path}
            )

        extension: str = file_path_obj.suffix.lower()

        # verificar extension
        if extension not in self.ALLOWED_EXTENSIONS:
            raise DomainException(
                "Tipo de archivo no soportado",
                details={
                    "file_path": file_path,
                    "extension": extension,
                    "allowed_extensions": self.ALLOWED_EXTENSIONS,
                },
            )

        return {
            "valid": True,
            "file_path": str(file_path_obj),
            "file_name": file_path_obj.name,
            "extension": extension,
        }

    def validate_files(
        self, files_paths: List[str]
    ) -> dict[str, List[dict[str, str]] | int]:
        valid_files: List[dict[str, str]] = []
        invalid_files: List[dict[str, str]] = []

        for file_path in files_paths:
            try:

                validation = self.validate_file(file_path)

                valid_files.append(validation)
            except DomainException as e:
                invalid_files.append({"file_path": file_path, "error": str(e)})

        return {
            "valid_files": valid_files,
            "invalid_files": invalid_files,
            "valid_files_count": len(valid_files),
            "invalid_files_count": len(invalid_files),
        }

    def load_document(self, file_path: str) -> List[LlamaDocument]:
        try:

            self.validate_file(file_path)

            reader = SimpleDirectoryReader(input_files=[file_path])

            documents: List[Document] = reader.load_data()

            if not documents:
                raise DomainException(
                    "No hay contenido para extraer del archivo",
                    details={"file_path": file_path},
                )

            return documents
        except Exception as e:
            raise DomainException(
                "Error al cargar los archivos",
                details={"path": file_path, "error": str(e)},
            )

    def load_documents_from_directory(self, directory_path: str, recursive: Optional[bool] = False) -> List[LlamaDocument]:
        try:
            path = Path(directory_path)

            if not path.exists():
                raise DomainException(
                    "No existe el directorio",
                    details={"directory_path": directory_path},
                )

            if not path.is_dir():
                raise DomainException(
                    "No es un directorio valido",
                    details={"directory_path": directory_path},
                )

            reader = SimpleDirectoryReader(input_dir=path, required_exts=self.ALLOWED_EXTENSIONS, recursive=recursive or False)

            documents: List[Document] = reader.load_data()

            for doc in documents:
                if not doc:
                    raise DomainException(
                        "No hay contenido para extraer del archivo",
                        details={"file_path": path},
                    )

            return documents
        except Exception as e:
            raise DomainException(
                "Error cargando documentos del directorio",
                details={"directory_path": directory_path, "error": str(e)},
            )
