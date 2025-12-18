from app.infrastructure.database.vector_store.chroma_client import ChromaClient
from app.infrastructure.llm.gemini.client import GeminiAdapter
from app.domain.factories.sql_agent_factory import SQLAgentFactory
from app.domain.agents.sql_agent.sql_agent import SQLAgent
from app.config.settings import Settings
from functools import lru_cache


@lru_cache
def get_settings() -> Settings:
    return Settings()  # type: ignore


def get_vector_store() -> ChromaClient:
    settings = get_settings()

    return ChromaClient(
        collection_name=settings.chroma_collection,
        persist_directory=settings.chroma_path,
    )


def get_llm_client() -> GeminiAdapter:
    settings = get_settings()

    return GeminiAdapter(
        llm_model_name=settings.llm_gemini_model,
        api_key=settings.google_api_key,
        embed_model=settings.embed_model_name,
    )


def get_sql_agent_factory() -> SQLAgentFactory:
    return SQLAgentFactory(llm_client=get_llm_client(), vector_store=get_vector_store())


def get_sql_agent() -> SQLAgent:
    settings = get_settings()

    sql_agent = get_sql_agent_factory().create_sql_agent(settings.agent_sql_name)

    return sql_agent
