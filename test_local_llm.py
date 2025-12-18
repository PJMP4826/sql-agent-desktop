from app.infrastructure.llm.local_llm.lm_studio.client import LmStudioAdapter
from llama_index.core.agent.workflow import FunctionAgent
from app.config.settings import Settings
from llama_index.core.workflow import Context
import asyncio


class Agent:
    def __init__(self) -> None:
        self.settings = Settings()  # type: ignore

        self.llm_client = LmStudioAdapter(
            llm_model_name=self.settings.llm_local_model_name,
            base_url=self.settings.base_url_local_llm_host,
            api_key=self.settings.google_api_key,
            embed_model=self.settings.embed_model_name,
        )

        self._create_agent()
        self._create_chat_history()

    def _create_agent(self):
        self.agent = FunctionAgent(
            name="Agente CFDI",
            llm=self.llm_client.get_llm_model()
        )

    def _create_chat_history(self):
        self.context_chat_history = Context(self.agent)
    
    async def chat(self, mensaje: str) -> str:
        try:
            response = await self.agent.run(mensaje, ctx=self.context_chat_history)
            return str(response)
        except Exception as e:
            print(f"Error en el agente: {str(e)}")
            return f"Lo siento, hubo un error procesando tu mensaje: {str(e)}"

async def main():
    try:
        while True:
            user_input = input("Tu: ")
            if user_input.lower() in ["salir", "exit"]:
                print("Adios")
                break

            agent = Agent()

            response = await agent.chat(mensaje=user_input)
            print(f"Bot: {response}")

    except (ValueError, RuntimeError) as e:
        print(f"Error fatal durante la iniciapizacion del bot: {e}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Error: {str(e)}")
