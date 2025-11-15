import os
import asyncio
from src.core.chat_query_engine import ChatQueryEngine
from llama_index.core.agent.workflow import ReActAgent
from llama_index.core.tools import FunctionTool
from llama_index.core.agent.workflow import FunctionAgent
from src.config.initialize_models import initialize_models
from src.core.schema_loader import SchemaLoader
from pathlib import Path


class AgentHandler:
    def __init__(self):
        self.table_retriever = SchemaLoader()
        self.cargarRolBot()
        self.models = initialize_models()
        self._create_tools()
        self._create_agent()

    def cargarRolBot(self):
        directorio_actual = Path(os.path.dirname(os.path.abspath(__file__)))

        ruta_absoluta_txt = (
            directorio_actual.parent.parent.parent / "config" / "rol_bot_sql.txt"
        )

        with open(ruta_absoluta_txt, "r", encoding="utf-8") as f:
            rol_bot = f.read()

        self.system_prompt_rol = rol_bot

    def _create_tools(self):
        consultar_base_datos = FunctionTool.from_defaults(
            fn=self._consultar_db_directo,
            name="consultar_base_datos",
            description=(
                "Consulta la base de datos de CONTPAQi® Comercial usando lenguaje natural"
                "Traduce automáticamente la pregunta a SQL y ejecuta la consulta.\n\n"
                "Úsala para preguntas sobre:\n"
                "- Ventas, facturación, ingresos\n"
                "- Clientes, proveedores, agentes\n"
                "- Inventarios, productos, almacenes\n"
                "- Documentos, pagos, saldos\n"
                "- Análisis, reportes, estadísticas\n\n"
                "Entrada: Pregunta completa en lenguaje natural\n"
                "Salida: Datos estructurados/lenguaje natural con la respuesta"
            ),
        )

        self.tools = [consultar_base_datos]

    def _create_agent(self):
        self.agent = FunctionAgent(
            name="Agente CFDI",
            llm=self.models["llm"],
            tools=self.tools,
            system_prompt=self.system_prompt_rol,
        )

    def _consultar_db_directo(self, query: str):
        try:
            include_tables: list[str] = self.table_retriever.inferir_tables_from_query(
                query
            )
            chat_engine = ChatQueryEngine(include_tables=include_tables)
            chat_engine.include_tables = include_tables
            response = chat_engine.sql_query_engine.query(query)

            return str(response)
        except Exception as e:
            error_msg = f"Error procesando la consulta: {str(e)}"
            print(error_msg)

    async def chat(self, mensaje: str) -> str:
        try:
            response = await self.agent.run(mensaje)
            return str(response)
        except Exception as e:
            print(f"Error en el agente: {str(e)}")
            return f"Lo siento, hubo un error procesando tu mensaje: {str(e)}"

    async def run_chat(self):
        while True:
            try:
                query = input("\n Escribe: ")

                if query in ["salir", "exit"]:
                    print("Cerrando...")
                    break

                if not query:
                    print("Pregunta invalida")

                print("Procesando")
                response = await self.chat(query)

                if response:
                    print(f"\n Respuesta: {response}")

            except Exception as e:
                print(f"\n Error: {str(e)}")
