from app.domain.services.context_builder import ContextBuilder
from app.infrastructure.database.vector_store.chroma_client import ChromaClient
from app.infrastructure.llm.gemini.client import GeminiAdapter
from app.config.settings import Settings
import logging
from app.domain.agents.rag_agent.prompts.system_prompts import RagPrompts
from app.domain.services.table_classifier import TableClassifier
from app.domain.factories.rag_factory import RagServiceFactory


logging.basicConfig(
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

settings = Settings()  # type: ignore

vector_store = ChromaClient(
    collection_name="test_collection", persist_directory="./data/vector_store/chroma"
)

try:
    gemini_client = GeminiAdapter(
        llm_model_name=settings.llm_gemini_model,
        api_key=settings.google_api_key,
        embed_model=settings.embed_model_name,
    )
    logger.info("Cliente Gemini inicializado exitosamente")
except Exception as e:
    logger.error(f"Fallo al inicializar Gemini: {e}")
    raise


system_prompt_clasificador = RagPrompts.get_prompt("clasificador_tablas")
system_prompt_general = RagPrompts.get_prompt("general")


rag_factory = RagServiceFactory(
    vector_store=vector_store,
    llm_client=gemini_client,
)

classifier_rag = rag_factory.create_classifier_rag()

general_rag = rag_factory.create_general_rag()


table_classifier = TableClassifier(rag_service=classifier_rag)

context = ContextBuilder(rag_service=general_rag)


def main():
    try:
        while True:
            user_input = input("Tu: ")
            if user_input.lower() in ["salir", "exit"]:
                print("Adios")
                break

            tables_string: str = classifier_rag.chat(user_input=user_input)

            tables_list: list[str] = table_classifier.inferir_tables(tables_string)

            response = context.build_context(
                user_query=user_input, selected_tables=tables_list
            )
            print(f"Business context: {response}")

    except (ValueError, RuntimeError) as e:
        print(f"Error fatal durante la iniciapizacion del bot: {e}")

if __name__ == "__main__":
    main()