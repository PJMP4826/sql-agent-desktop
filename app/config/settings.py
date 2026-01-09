import sys
from pydantic_settings import BaseSettings
from pydantic import Field, ConfigDict
from pathlib import Path


def get_base_path() -> Path:
    """Obtiene la ruta base del proyecto"""
    if getattr(sys, "frozen", False):
        # si la app esta empaquetada con PyInstaller
        return Path(sys.executable).parent
    else:
        # si es script o Docker
        return Path(__file__).resolve().parent.parent.parent


BASE_DIR = get_base_path()


class Settings(BaseSettings):

    model_config = ConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )  # type: ignore

    # LLM Configuracion
    google_api_key: str = Field(..., description="Google API Key")
    llm_gemini_model: str = Field(..., description="Gemini Model")
    embed_model_name: str = Field(..., description="Embedding model")

    # Database configuration
    db_user: str = Field(..., description="Database username")
    db_password: str = Field(..., description="Database password")
    db_name: str = Field(..., description="Database name")
    db_port: str = Field(default="1433", description="Database port")
    db_host: str = Field(..., description="Database host")

    # RAG Client Configuration
    rag_client_base_url: str = Field(..., description="URL base de los endpoints")

    # Agents Configurations
    agent_sql_name: str = Field(..., description="Nombre de Agent SQL")

    

    @property
    def database_url(self) -> str:
        return (
            f"mssql+pyodbc://{self.db_user}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
            f"?driver=ODBC+Driver+17+for+SQL+Server"
        )

settings = Settings()  # type: ignore
