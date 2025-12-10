import asyncio
from app.infrastructure.llm.gemini.client import GeminiAdapter
from app.config.settings import Settings
from app.application.ports.llm_port import LLMPort


class Test:
    def __init__(self, llm_client: LLMPort) -> None:
        self.llm_client = llm_client

    def generate_response(self, user: str) -> str:
        try:
            print("Procesando")
            response = self.llm_client.generate_response(user)

            return response
        except Exception as e:
            raise Exception(f"Error: {str(e)}")


if __name__ == "__main__":

    setting = Settings()

    ai = GeminiAdapter(
        setting.llm_gemini_model, setting.google_api_key, setting.embed_model_name
    )

    test = Test(ai)

    while True:

        async def main_async_completion_cli():
            try:
                user = input("\n Escribe: ")
                
                response = await ai.generate_async_response_stream(user)

                async for r in response:
                    print(r.text, end="", flush=True)
                print("\n")

                # if response:
                #     print(f"\n Respuesta: {response}")
            except Exception as e:
                print(f"\n Error: {str(e)}")

        asyncio.run(main_async_completion_cli())
