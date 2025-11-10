import os
from dotenv import load_dotenv
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
EMBED_MODEL_NAME = os.getenv("EMBED_MODEL_NAME")
LLM_MODEL = os.getenv("LLM_MODEL")

def validate_env():
    env_requeridas = ["GOOGLE_API_KEY", "EMBED_MODEL_NAME", "LLM_MODEL"]
    faltantes = []

    for var in env_requeridas:
        value = os.getenv(var)
        if value is None or value.strip() == "":
            faltantes.append(var)

    if faltantes:
        raise EnvironmentError(
            f"Variables de entorno faltantes: {', '.join(faltantes)}"
        )

def initialize_models() -> dict:
    validate_env()

    llm = GoogleGenAI(model=LLM_MODEL)
    embed_model = GoogleGenAIEmbedding(model_name=EMBED_MODEL_NAME, api_key=API_KEY)

    return {"llm": llm, "embed_model": embed_model}

