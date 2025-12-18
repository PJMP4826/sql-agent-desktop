from app.infrastructure.database.vector_store.chroma_client import ChromaClient
from app.infrastructure.llm.gemini.client import GeminiAdapter
from app.domain.factories.sql_agent_factory import SQLAgentFactory
from app.config.settings import Settings
import logging
import asyncio

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main():
    settings = Settings() # type: ignore
    
    # 1. Inicializar infraestructura
    vector_store = ChromaClient(
        collection_name=settings.chroma_collection,
        persist_directory=settings.chroma_path
    )
    
    gemini_client = GeminiAdapter(
        llm_model_name=settings.llm_gemini_model,
        api_key=settings.google_api_key,
        embed_model=settings.embed_model_name
    )
    
    # 2. Verificar que hay documentos indexados
    if vector_store.get_collection_count() == 0:
        logger.error("No documents indexed! Index schema documentation first.")
        return
    
    # 3. Crear SQL Agent usando factory
    factory = SQLAgentFactory(
        llm_client=gemini_client,
        vector_store=vector_store
    )
    
    sql_agent = factory.create_sql_agent(agent_name="Asistente Contable")    
    
    try:
        while True:
            user_input = input("Tu: ").strip()
            
            if user_input.lower() in ["salir", "exit", "quit"]:
                print("Adios!")
                break
            
            if not user_input:
                continue
            
            try:
                response = await sql_agent.chat(user_input)
                print(f"\nAgent: {response}\n")
            except Exception as e:
                print(f"\nError: {e}\n")
    
    except KeyboardInterrupt:
        print("\n\nInterrupted. Goodbye!")
    except Exception as e:
        logger.exception(f"Fatal error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
