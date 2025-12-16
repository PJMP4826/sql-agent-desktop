from app.infrastructure.database.vector_store.chroma_client import ChromaClient
from app.domain.services.rag_service import RagService
from app.infrastructure.llm.gemini.client import GeminiAdapter
from app.config.settings import Settings
import logging

logging.basicConfig(
    level=logging.INFO,
)
logger = logging.getLogger(__name__)
settings = Settings() # type: ignore
    
logger.info(f"Modelo LLM: {settings.llm_gemini_model}")
logger.info(f"Modelo Embed: {settings.embed_model_name}")

vector_store = ChromaClient(
    collection_name='test_collection',
    persist_directory='./data/vector_store/chroma'
)

logger.info(f"Vector store inicializado. Conteo: {vector_store.get_collection_count()}")

try:
    gemini_client = GeminiAdapter(
        llm_model_name=settings.llm_gemini_model,
        api_key=settings.google_api_key,
        embed_model=settings.embed_model_name
    )
    logger.info("Cliente Gemini inicializado exitosamente")
except Exception as e:
    logger.error(f"Fallo al inicializar Gemini: {e}")
    raise

system_prompt = """
    Eres un clasificador experto cuya unica funcion es 
    identificar que tablas de una base de datos son relevantes
    para responder la peticion del usuario.

    Tu output debe ser unicamente un array de 
    strings, sin texto adicional, en texto plano, sin explicaciones, 
    sin comentarios, sin SQL.

    Ejemplo de salida valida:
    ["table1", "table2"]

    Reglas estrictas:
    - Analiza correctamente el schema de la BD
    - Selecciona la tabla si tiene alta probabilidad de ser necesaria
    - Usa razonamiento semantico
    - Si ninguna tabla aplica, devuelve []
    - No expliques tu seleccion
    """


rag = RagService(
        vector_store=vector_store,
        llm_client=gemini_client,
        system_prompt=system_prompt,  
        auto_index_on_empty=False  
    )

def main():
    try:
        current_count = vector_store.get_collection_count()
        logger.info(f"Conteo de documentos actual: {current_count}")
        
        if current_count == 0:
            logger.info("Vector store vacio, indexando documentos...")
            
            result = rag.index_directory("./books")
            
            logger.info(f"Resultado de indexacion: {result}")
            
            post_count = vector_store.get_collection_count()
            logger.info(f"CONTEO POST-INDEXACION: {post_count}")
            
            if post_count == 0:
                logger.error("Indexacion completada pero el conteo sigue siendo 0!")
                logger.error("Verifique si el directorio ./docs existe y tiene documentos")
                return
        else:
            logger.info(f"Vector store ya tiene {current_count} documentos")
        
        logger.info("Probando funcionalidad de chat...")
        response = rag.chat("Muestrame las tablas de clientes")
        logger.info(f"Respuesta del Chat: {response}")
                
    except Exception as e:
        logger.exception(f"Error durante la ejecucion: {e}")
        raise


def test_index_file():
    try:
        current_count = vector_store.get_collection_count()
        logger.info(f"Conteo de documentos actual: {current_count}")

        file_path = "./COM_BDD_CONTEXT_merged.pdf"
        result = rag.add_document(file_path=file_path)

        logger.info(f"Resultado de indexacion: {result}")
        post_count = vector_store.get_collection_count()
        if post_count == 0:
            logger.error("Indexacion completada pero el conteo sigue siendo 0!")
            logger.error(f"Verifique si el directorio {file_path} existe y tiene informacion")
            return
    
    except Exception as e:
        logger.exception(f"Error durante la ejecucion: {e}")
        raise


if __name__ == "__main__":
    test_index_file()