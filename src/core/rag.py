import os
import logging
from pathlib import Path
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.core import StorageContext
from src.core.chroma_client import Chroma
from src.config.initialize_models import initialize_models

logging.disable(logging.CRITICAL)


class RAG:
    def __init__(self, docs_path: str = None):
        self.modelos = initialize_models()

        if docs_path is None:
            current_file = Path(__file__)
            project_root = current_file.parent.parent.parent
            self.docs_path = str(project_root / "docs")
        else:
            self.docs_path = docs_path

        self._initialize_components()
        self._setup_engine()

    def _initialize_components(self):
        self.llm = self.modelos["llm"]
        self.embed_model = self.modelos["embed_model"]

        Settings.llm = self.llm
        Settings.embed_model = self.embed_model

    def cargarRolBot(self) -> str:
        directorio_actual = Path(os.path.dirname(os.path.abspath(__file__)))

        ruta_absoluta_txt = directorio_actual.parent / "config" / "rol_bot_table_selector.txt"

        with open(ruta_absoluta_txt, "r", encoding="utf-8") as f:
            rol_bot = f.read()

        return rol_bot

    def _setup_engine(self):
        try:

            chroma = Chroma("sql_bot", "./sql_bot")

            if chroma.createChromaCollection().count() == 0:
                print("Indexando documentos en la BD")
                documents = SimpleDirectoryReader(self.docs_path).load_data()
                storage_context = StorageContext.from_defaults(
                    vector_store=chroma.vectorStore()
                )
                index = VectorStoreIndex.from_documents(
                    documents, storage_context=storage_context
                )
            else:
                print("Usando documentos ya indexados en ChromaDB")
                index = VectorStoreIndex.from_vector_store(
                    embed_model=self.embed_model, vector_store=chroma.vectorStore()
                )

            self.query_engine = index.as_query_engine()

            self.chat_engine = index.as_chat_engine(
                chat_mode="condense_plus_context",
                system_prompt=(self.cargarRolBot()),
                verbose=False,
            )
        except Exception as e:
            raise RuntimeError(f"Error al cargar los documentos o motorea{e}")

    def procesar_query(self, user_input: str):
        try:
            resp = self.chat_engine.chat(user_input)
            return str(resp)
        except Exception as e:
            return f"Lo siento, hubo un problema al procesar la solicitud {e}"
