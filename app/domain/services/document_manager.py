import os
from typing import List, Optional
from llama_index.core import (
    SimpleDirectoryReader,
    Document as LlamaDocument,
)
from app.application.ports.vector_store_port import VectorStorePort
from app.shared.domain_exceptions import DomainException
from llama_index.core.schema import Document


class DocumentManager:
    def __init__(self, vector_store: VectorStorePort) -> None:
        self.vector_store = vector_store
        self.file_extensions = [".pdf", ".txt", ".md", ".docx", ".doc"]

    
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

    