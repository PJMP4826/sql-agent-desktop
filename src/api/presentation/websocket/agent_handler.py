import asyncio
from src.core.chat_query_engine import ChatQueryEngine
from llama_index.core.agent.workflow import ReActAgent
from llama_index.core.tools import FunctionTool
from llama_index.core.agent.workflow import FunctionAgent
from src.config.initialize_models import initialize_models


class AgentHandler:
    def __init__(self):
        self.chat_engine = ChatQueryEngine()
        self.system_prompt = self.chat_engine.system_prompt_rol
        self.models = initialize_models()
        self._create_tools()
        self._create_agent()

    def _create_tools(self):
        consultar_base_datos = FunctionTool.from_defaults(
            fn=self._consultar_db_directo,
            name="consultar_base_datos",
            description=(
                "Consulta la base de datos de CFDIs (facturas electrónicas mexicanas) usando lenguaje natural. "
                "Esta herramienta traduce automáticamente tu pregunta a SQL y ejecuta la consulta.\n\n"
                "Úsala cuando el usuario pregunte sobre:\n"
                "- Ventas, ingresos, facturación o totales\n"
                "- Información de clientes o receptores\n"
                "- Pagos recibidos y métodos de pago\n"
                "- Impuestos (IVA, ISR, retenciones) y deducciones\n"
                "- Estadísticas, reportes o análisis de datos fiscales\n"
                "- Conceptos facturados, productos o servicios\n"
                "- Fechas, periodos o rangos temporales\n\n"
                "IMPORTANTE:\n"
                "- Pasa la pregunta COMPLETA del usuario tal cual\n"
                "- NO intentes reformular o simplificar la pregunta\n"
                "- Incluye todos los detalles: fechas, nombres, montos, etc.\n\n"
                "Entrada: Pregunta en lenguaje natural (ej: '¿Cuánto vendí en enero 2024?')\n"
                "Salida: Datos estructurados con la respuesta a la consulta"
            ),
        )

        self.tools = [consultar_base_datos]

    def _create_agent(self):
        self.agent = FunctionAgent(
            name="Agente CFDI",
            llm=self.models["llm"],
            tools=self.tools,
            system_prompt=self.system_prompt,
        )

    def _consultar_db_directo(self, query: str):
        try:
            response = self.chat_engine.sql_query_engine.query(query)

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
