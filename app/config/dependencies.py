from app.infrastructure.llm.gemini.client import GeminiAdapter
from app.domain.factories.sql_agent_factory import SQLAgentFactory
from app.domain.agents.sql_agent.sql_agent import SQLAgent
from app.api.http.controllers.document_controller import DocumentController
from app.infrastructure.repositories.document_repository import DocumentRepository
from app.config.settings import Settings
from functools import lru_cache
from app.domain.services.token_counter import TokenCounter
from llama_index.core.callbacks import CallbackManager, TokenCountingHandler


@lru_cache
def get_settings() -> Settings:
    return Settings()  # type: ignore



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


def create_sql_agent() -> SQLAgent:
    settings = get_settings()

    factory = SQLAgentFactory(
        llm_client=create_llm_client()
    )

    return factory.create_sql_agent(settings, settings.agent_sql_name)


def get_document_repository() -> DocumentRepository:
    return DocumentRepository()


def get_document_controller() -> DocumentController:
    repository = get_document_repository()
    return DocumentController(repository=repository)
