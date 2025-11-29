import os
import asyncio
from src.core.chat_query_engine import ChatQueryEngine
from llama_index.core.agent.workflow import ReActAgent
from llama_index.core.tools import FunctionTool
from llama_index.core.agent.workflow import FunctionAgent
from src.config.initialize_models import initialize_models
from src.core.schema_loader import SchemaLoader
from llama_index.core.workflow import Context
from pathlib import Path


class AgentHandler:
    def __init__(self):
        self.table_retriever = SchemaLoader()
        self.cargarRolBot()
        self.models = initialize_models()
        self._create_tools()
        self._create_agent()
        self.max_iterations = 5 
        self.current_iterations = 0

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
        self.context_chat_history = Context(self.agent)

    def _consultar_db_directo(self, query: str):
        try:
            # validar que la query no este vacia
            if not query or not query.strip():
                return "Error: La consulta está vacía. Por favor proporciona una pregunta válida."

            include_tables: list[str] = self.table_retriever.inferir_tables_from_query(
                query
            )

            # validar que se haya tablas
            if not include_tables:
                return (
                    "Error: No se pudieron identificar tablas relevantes para tu consulta. "
                    "Por favor reformula tu pregunta o especifica mejor qué información necesitas."
                )

            # validar que hay al menos una tabla conocida
            if len(include_tables) == 0:
                return "Error: Ninguna de las tablas inferidas es válida. Intenta reformular tu pregunta."

            # obtener contexto de negocio
            business_context = self.table_retriever.obtener_contexto_negocio(
                query, include_tables
            )

            if not business_context or business_context.strip() == "":
                print(
                    "Advertencia: No se pudo obtener contexto de negocio. Continuando sin él."
                )
                business_context = f"Tablas a usar: {', '.join(include_tables)}"

            # crear engine
            chat_engine = ChatQueryEngine(
                include_tables=include_tables, business_context=business_context
            )

            if (
                not hasattr(chat_engine, "sql_query_engine")
                or chat_engine.sql_query_engine is None
            ):
                return "Error: No se pudo inicializar el motor de consultas SQL. Verifica la conexión a la base de datos."

            response = chat_engine.sql_query_engine.query(query)

            if response is None:
                return "Error: La consulta no devolvió resultados. Verifica los filtros o la pregunta."

            return str(response)

        except ValueError as e:
            error_msg = f"Error de validación: {str(e)}"
            print(error_msg)
            return error_msg
        except Exception as e:
            error_msg = f"Error procesando la consulta: {str(e)}"
            print(error_msg)
            return f"Lo siento, ocurrió un error: {str(e)}. Por favor intenta reformular tu pregunta."

    async def chat(self, mensaje: str) -> str:
        try:
            # reiniciar contador de iteraciones
            self.current_iterations = 0

            # limite de iteracione
            response = await self.agent.run(mensaje, ctx=self.context_chat_history)

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
