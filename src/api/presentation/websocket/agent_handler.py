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
        consulta_sql_tool = FunctionTool.from_defaults(
            fn=self.chat_engine.procesar_query,
            name="consultar_base_datos",
            description=(
                "Herramienta para consultar la base de datos de CFDIs (facturas electrónicas). "
                "Úsala cuando el usuario pregunte sobre:\n"
                "- Ventas, facturas, totales\n"
                "- Información de clientes\n"
                "- Pagos recibidos\n"
                "- Impuestos y deducciones\n"
                "- Estadísticas o reportes\n"
                "- Cualquier dato relacionado con facturación\n\n"
                "Input: Pregunta en lenguaje natural sobre los datos fiscales.\n"
                "Output: Respuesta con los datos solicitados y análisis."
            ),
        )

        self.tools = [consulta_sql_tool]

    def _create_agent(self):
        self.agent = FunctionAgent(
            name="Agente CFDI",
            llm=self.models["llm"],
            tools=self.tools,
            system_prompt=self.system_prompt,
        )

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
