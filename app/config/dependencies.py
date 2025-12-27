from app.infrastructure.database.vector_store.qdrant_client import (
    QdrantVectorStoreClient,
)
from app.infrastructure.llm.gemini.client import GeminiAdapter
from app.domain.factories.sql_agent_factory import SQLAgentFactory
from app.domain.agents.sql_agent.sql_agent import SQLAgent
from app.api.http.controllers.document_controller import DocumentController
from app.domain.repositories.document_repository import DocumentRepository
from app.config.settings import Settings
from functools import lru_cache

_sql_agent: SQLAgent | None = None


@lru_cache
def get_settings() -> Settings:
    return Settings()  # type: ignore


def get_vector_store() -> QdrantVectorStoreClient:
    settings = get_settings()

    return QdrantVectorStoreClient(
        collection_name=settings.qdrant_collection, url=settings.qdrant_url_server
    )


def get_llm_client() -> GeminiAdapter:
    settings = get_settings()

    return GeminiAdapter(
        llm_model_name=settings.llm_gemini_model,
        api_key=settings.google_api_key,
        embed_model=settings.embed_model_name,
    )


def get_sql_agent() -> SQLAgent:
    settings = get_settings()

    global _sql_agent

    if _sql_agent is None:
        factory = SQLAgentFactory(
            llm_client=get_llm_client(), vector_store=get_vector_store()
        )

        _sql_agent = factory.create_sql_agent(settings.agent_sql_name)

    return _sql_agent


def reset_sql_agent():
    global _sql_agent
    _sql_agent = None


def get_document_repository() -> DocumentRepository:
    return DocumentRepository()


def get_document_controller() -> DocumentController:
    repository = get_document_repository()

    return DocumentController(repository=repository)
