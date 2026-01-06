from app.infrastructure.database.vector_store.qdrant_client import QdrantVectorStoreClient
# from app.domain.services.rag_service import RagService
from app.domain.factories.rag_factory import RagServiceFactory
from app.infrastructure.llm.gemini.client import GeminiAdapter
from app.config.settings import Settings
from app.domain.agents.rag_agent.prompts.system_prompts import RagPrompts
import logging
from functools import lru_cache
from app.domain.services.token_counter import TokenCounter
from llama_index.core.callbacks import CallbackManager, TokenCountingHandler


logging.basicConfig(
    level=logging.INFO,
)

logger = logging.getLogger(__name__)
settings = Settings() # type: ignore
    
logger.info(f"Modelo LLM: {settings.llm_gemini_model}")
logger.info(f"Modelo Embed: {settings.embed_model_name}")

@lru_cache
def get_settings() -> Settings:
    return Settings()  # type: ignore

def get_vector_store() -> QdrantVectorStoreClient:
    settings = get_settings()
    return QdrantVectorStoreClient(
        collection_name=settings.qdrant_collection, url=settings.qdrant_url_server
    )

vector_store = get_vector_store()

logger.info(f"Vector store inicializado. Conteo: {vector_store.get_collection_count()}")


def create_token_counting_handler() -> TokenCountingHandler:
    return TokenCountingHandler(verbose=True)


def create_callback_manager() -> tuple[TokenCountingHandler, CallbackManager]:
    token_counting_handler = create_token_counting_handler()

    return token_counting_handler, CallbackManager([token_counting_handler])


def create_token_counter() -> TokenCounter:
    token_counting_handler, callback_manager = create_callback_manager()

    return TokenCounter(
        token_counting_handler=token_counting_handler,
        callback_manager=callback_manager,
    )


def create_llm_client() -> GeminiAdapter:
    settings = get_settings()

    return GeminiAdapter(
        llm_model_name=settings.llm_gemini_model,
        api_key=settings.google_api_key,
        embed_model=settings.embed_model_name,
        token_counter=create_token_counter(),
    )

try:
    gemini_client = create_llm_client()
    logger.info("Cliente Gemini inicializado exitosamente")
except Exception as e:
    logger.error(f"Fallo al inicializar Gemini: {e}")
    raise

system_prompt = RagPrompts.get_prompt("general")


rag_factory = RagServiceFactory(
    vector_store=vector_store,
    llm_client=gemini_client,
)

classifier_rag = rag_factory.create_general_rag()

def main():
    try:
        current_count = vector_store.get_collection_count()
        logger.info(f"Conteo de documentos actual: {current_count}")
        
        if current_count == 0:
            logger.info("Vector store vacio, indexando documentos...")
            
            directory: str = "./books"
            result = classifier_rag.index_directory(directory=directory)
            
            logger.info(f"Resultado de indexacion: {result}")
            
            post_count = vector_store.get_collection_count()
            logger.info(f"CONTEO POST-INDEXACION: {post_count}")
            
            if post_count == 0:
                logger.error("Indexacion completada pero el conteo sigue siendo 0!")
                logger.error(f"Verifique si el directorio {directory} existe y tiene documentos")
                return
        else:
            logger.info(f"Vector store ya tiene {current_count} documentos")
        
        logger.info("Probando funcionalidad de chat...")
        response = classifier_rag.chat("Muestrame las tablas de clientes")
        logger.info(f"Respuesta del Chat: {response}")
                
    except Exception as e:
        logger.exception(f"Error durante la ejecucion: {e}")
        raise


def test_index_file():
    try:
        current_count = vector_store.get_collection_count()
        logger.info(f"Conteo de documentos actual: {current_count}")

        file_path = "./COM_BDD_CONTEXT_merged.pdf"
        result = classifier_rag.add_document(file_path=file_path)

        logger.info(f"Resultado de indexacion: {result}")
        post_count = vector_store.get_collection_count()
        if post_count == 0:
            logger.error("Indexacion completada pero el conteo sigue siendo 0!")
            logger.error(f"Verifique si el directorio {file_path} existe y tiene informacion")
            return
    
    except Exception as e:
        logger.exception(f"Error durante la ejecucion: {e}")
        raise

def test_rag():
     while True:
            user_input = input("Tu: ").strip()
            
            if user_input.lower() in ["salir", "exit", "quit"]:
                print("Adios!")
                break
            
            if not user_input:
                continue
            
            try:
                response = classifier_rag.chat(user_input)
                print(f"\nAgent: {response}\n")
            except Exception as e:
                print(f"\nError: {e}\n")


if __name__ == "__main__":
    test_rag()