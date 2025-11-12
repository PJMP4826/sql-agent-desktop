import os
from pathlib import Path
from dotenv import load_dotenv
from typing import List, Optional, Dict
from src.config.initialize_models import initialize_models, initialize_db_credentials
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core.base.llms.types import ChatMessage, MessageRole
from sqlalchemy import create_engine
from llama_index.core import SQLDatabase
from llama_index.core.query_engine import NLSQLTableQueryEngine
from llama_index.core.chat_engine import CondenseQuestionChatEngine

load_dotenv()


class ChatQueryEngine:
    def __init__(self):
        self.system_prompt_rol = ""
        self.cargarRolBot()
        self._initialize_components()
        self._initalize_database()

    def cargarRolBot(self):
        directorio_actual = Path(os.path.dirname(os.path.abspath(__file__)))

        ruta_absoluta_txt = directorio_actual.parent / "config" / "rol_bot_sql.txt"

        with open(ruta_absoluta_txt, "r", encoding="utf-8") as f:
            rol_bot = f.read()

        self.system_prompt_rol = rol_bot

    def _initialize_components(self):
        models = initialize_models()

        self.llm = models["llm"]

        self.embed_model = models["embed_model"]

        self.memory = ChatMemoryBuffer.from_defaults(
            chat_history=[
                ChatMessage(role=MessageRole.SYSTEM, content=self.system_prompt_rol)
            ],
            token_limit=2500,
        )

    def _initalize_database(self):
        credentials = initialize_db_credentials()
        db_user: str = credentials["db_user"]
        db_password: str = credentials["db_password"]
        db_name: str = credentials["db_name"]
        db_port: str = credentials["db_port"]
        db_host: str = credentials["db_host"]

        self.db_engine = create_engine(
            f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}?client_encoding=UTF8",
            echo=False,
            pool_pre_ping=True,
            pool_recycle=3600,
        )

        self.include_tables = [
            "cancelaciones",
            "cfdisrelacionados",
            "conceptos",
            "configuracion",
            "documentos",
            "documentosrelpago",
            "emisor",
            "impuestos",
            "pagos",
            "receptor",
        ]

        self.sql_database = SQLDatabase(
            self.db_engine, include_tables=self.include_tables
        )

        #natural language a SQL
        self.sql_query_engine = NLSQLTableQueryEngine(
            sql_database=self.sql_database,
            tables=self.include_tables,
            llm=self.llm,
            embed_model=self.embed_model,
            synthesize_response=True,
            verbose=True,
        )

        #para responder usando el contexto de la conversacion
        self.chat_engine = CondenseQuestionChatEngine.from_defaults(
            query_engine=self.sql_query_engine,
            memory=self.memory,
            verbose=False,
            llm=self.llm,
        )


# if __name__ == "__main__":
#     chat_engine = ChatQueryEngine()
#     print(chat_engine.db_host)
