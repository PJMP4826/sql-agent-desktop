import os
import sys
from dotenv import load_dotenv
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding

load_dotenv()

API_KEY: str = os.getenv("GOOGLE_API_KEY") or ""
EMBED_MODEL_NAME: str = os.getenv("EMBED_MODEL_NAME") or ""
LLM_MODEL: str = os.getenv("LLM_GEMINI_MODEL") or ""

DB_USER: str = os.getenv("DB_USER") or ""
DB_PASSWORD: str = os.getenv("DB_PASSWORD") or ""
DB_NAME: str = os.getenv("DB_NAME") or ""
DB_PORT: str = os.getenv("DB_PORT") or ""
DB_HOST: str = os.getenv("DB_HOST") or ""


def validate_env(env_requeridas: list[str]) -> None:
    faltantes: list[str] = []

    for var in env_requeridas:
        value = os.getenv(var) or None
        if value is None or value.strip() == "":
            faltantes.append(var)

    if faltantes:
        raise EnvironmentError(
            f"Variables de entorno faltantes: {', '.join(faltantes)}"
        )


def initialize_models() -> dict:
    env_requeridas = ["GOOGLE_API_KEY", "EMBED_MODEL_NAME", "LLM_GEMINI_MODEL"]
    validate_env(env_requeridas=env_requeridas)

    llm = GoogleGenAI(model=LLM_MODEL)
    embed_model = GoogleGenAIEmbedding(model_name=EMBED_MODEL_NAME, api_key=API_KEY)

    return {"llm": llm, "embed_model": embed_model}


def initialize_db_credentials() -> dict:
    env_requeridas = ["DB_USER", "DB_PASSWORD", "DB_NAME", "DB_PORT", "DB_HOST"]
    validate_env(env_requeridas=env_requeridas)

    return {
        "db_user": DB_USER,
        "db_password": DB_PASSWORD,
        "db_name": DB_NAME,
        "db_port": DB_PORT,
        "db_host": DB_HOST,
    }
