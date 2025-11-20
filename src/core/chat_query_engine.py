from pathlib import Path
from dotenv import load_dotenv
from typing import List, Dict
from src.config.initialize_models import initialize_models, initialize_db_credentials
from llama_index.core.memory import ChatSummaryMemoryBuffer
from sqlalchemy import create_engine
from llama_index.core import SQLDatabase, StorageContext
from llama_index.core.query_engine import NLSQLTableQueryEngine
from llama_index.core.prompts import PromptTemplate

# from llama_index.core.base.llms.types import ChatMessage, MessageRole
# from llama_index.core.chat_engine import CondenseQuestionChatEngine

load_dotenv()


class ChatQueryEngine:
    def __init__(self, include_tables: List[str], business_context: str):
        self.chat_history: List[Dict] = []
        self.include_tables: List[str] = include_tables
        self.business_context = business_context
        self._initialize_components()
        self._initalize_database()

    def _create_storage_context(self):
        self.persist_dir = Path("./storage/sql_index")
        self.persist_dir.mkdir(parents=True, exist_ok=True)

        docstore_path = self.persist_dir / "docstore.json"

        if not docstore_path.exists():
            print("Creando nuevo StorageContext (no se encontro uno previo)")
            self.storage_context = StorageContext.from_defaults()
        else:
            print(f"Cargando StorageContext existente desde {self.persist_dir}")
            self.storage_context = StorageContext.from_defaults(
                persist_dir=str(self.persist_dir)
            )

    def _initialize_components(self):
        try:
            models = initialize_models()

            self.llm = models["llm"]

            self.embed_model = models["embed_model"]

            self.memory = ChatSummaryMemoryBuffer.from_defaults(
                llm=self.llm, token_limit=2000
            )
        except Exception as e:
            print("Error: ", str(e))

    def _initalize_database(self):
        try:
            credentials = initialize_db_credentials()
            db_user: str = credentials["db_user"]
            db_password: str = credentials["db_password"]
            db_name: str = credentials["db_name"]
            db_port: str = credentials["db_port"]
            db_host: str = credentials["db_host"]

            connection_url = (
                f"mssql+pyodbc://{db_user}:{db_password}"
                f"@{db_host}:{db_port}/{db_name}"
                f"?driver=ODBC+Driver+17+for+SQL+Server"
            )

            self.db_engine = create_engine(
                connection_url,
                echo=False,
                pool_pre_ping=True,
                pool_recycle=3600,
            )

            self._create_storage_context()

            print("Tables para el engine: ", self.include_tables)

            self.sql_database = SQLDatabase(
                self.db_engine,
                include_tables=self.include_tables,
            )

            contpaq_context = f"""
                Dado el siguiente esquema de base de datos (tablas y columnas):

                {{schema}}

                Tu objetivo es convertir la pregunta del usuario en una consulta SQL válida.

                REGLAS ESTRICTAS:
                1. NO inventes columnas, NO inventes tablas. Usa únicamente los nombres EXACTOS del esquema.
                2. NO asumas relaciones entre tablas. SOLO puedes conectar tablas mediante columnas que coincidan exactamente en nombre y tipo lógico.
                3. Si no hay forma confiable de relacionar varias tablas, limita la consulta a una sola tabla.
                4. Usa subconsultas únicamente si es estrictamente necesario y SOLO si existe una columna coincidente entre tablas.
                5. Prefiere consultas simples a consultas complejas. No optimices.
                6. NO agregues texto explicativo. NO agregues comentarios. SOLO genera SQL.
                7. NO uses funciones o sintaxis fuera de SQL Server.
                8. Si la pregunta del usuario es ambigua, asume la interpretación mas simple basada en el esquema.
                9. Siempre usa un TOP 20 para reducir la cantidad de registros que consultas

                FORMATO DE RESPUESTA:
                Devuelve exclusivamente una consulta SQL valida. Nada mas.

                Pregunta del usuario:
                {{query_str}}

                ContextoNegocio:
                {self.business_context}

                Usa el ContextoNegocio para entender qué significan 
                los campos de las tablas y generar el SQL correcto.

                SQLQuery:  
                """

            prompt_sql = PromptTemplate(contpaq_context)

            mostrar_sql = True
            # natural language a SQL
            self.sql_query_engine = NLSQLTableQueryEngine(
                sql_database=self.sql_database,
                tables=self.include_tables,
                llm=self.llm,
                embed_model=self.embed_model,
                text_to_sql_prompt=prompt_sql,
                synthesize_response=False,
                verbose=mostrar_sql,
            )

            self.storage_context.persist(persist_dir=str(self.persist_dir))

            # para responder usando el contexto de la conversacion
            # self.chat_engine = CondenseQuestionChatEngine.from_defaults(
            #     query_engine=self.sql_query_engine,
            #     memory=self.memory,
            #     verbose=False,
            #     llm=self.llm,
            # )

        except Exception as e:
            print("Error al inicializar components db: ", e)

    # def procesar_query(self, query: str) -> Optional[str]:
    #     try:
    #         response = self.chat_engine.chat(query)

    #         return str(response)
    #     except Exception as e:
    #         error_msg = f"Error procesando la consulta: {str(e)}"
    #         print(error_msg)
    #         return None

    # def procesar_query_json(self, query: str) -> Optional[Dict]:
    #     try:
    #         response = self.chat_engine.chat(
    #             f"""
    #             Responde estrictamente en JSON.
    #             Usa este formato: {{"status": "success", "data": [...resultados...]}}.
    #             Consulta: {query}
    #         """
    #         )

    #         text_response = str(response).strip()

    #         # intentar parsear JSON
    #         try:
    #             json_response = json.loads(text_response)
    #         except json.JSONDecodeError:
    #             # intenta limpiar
    #             json_text = re.search(r"\{.*\}", text_response, re.DOTALL)
    #             if json_text:
    #                 json_response = json.loads(json_text.group(0))
    #             else:
    #                 json_response = {"status": "error", "message": text_response}

    #         self.chat_history.append({"user": query, "assistant": json_response})
    #         return json_response

    #     except Exception as e:
    #         error_message = f"Error procesando la consulta: {str(e)}"
    #         print(error_message)
    #         return {"status": "error", "message": error_message}

    # def run_chat(self):
    #     while True:
    #         try:
    #             query = input("\n Escribe: ")

    #             if query in ["salir", "exit"]:
    #                 print("Cerrando...")
    #                 break

    #             if not query:
    #                 print("Pregunta invalida")

    #             print("Procesando (con contexto)")
    #             response = self.procesar_query(query)

    #             if response:
    #                 print(f"\n Respuesta: {response}")

    #         except Exception as e:
    #             print(f"\n Error: {str(e)}")
