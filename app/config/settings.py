from pydantic_settings import BaseSettings
from pydantic import Field, ConfigDict
from pathlib import Path


class Settings(BaseSettings):
    model_config = ConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    # LLM Configuracion
    google_api_key: str = Field(..., description="Google API Key")
    llm_gemini_model: str = Field(..., description="Gemini Model")
    embed_model_name: str = Field(..., description="Embedding model")

    # Database configuration
    db_user: str = Field(..., description="Database username")
    db_password: int = Field(..., description="Database password")
    db_name: str = Field(..., description="Database name")
    db_port: int = Field(default="1433", description="Database port")
    db_host: str = Field(..., description="Database host")

    # Vector Store Configuration
    chroma_path: str = Field(
        default="./chroma_db", description="Path to ChromaDB storage"
    )
    chroma_collection: str = Field(
        default="sql_bot", description="ChromaDB collection name"
    )

    # Application Paths
    docs_path: str = Field(default="./docs", description="Path documents directory")
    storage_path: str = Field(
        default="./storage", description="Path application storage"
    )
    sql_index_path: str = Field(
        default="./storage/sql_index", description="Path SQL index storage"
    )

    @property
    def database_url(self) -> str:
        return (
            f"mssql+pyodbc://{self.db_user}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
            f"?driver=ODBC+Driver+17+for+SQL+Server"
        )

    @property
    def docs_path_resolved(self) -> Path:
        return Path(self.docs_path).resolve()

    @property
    def storage_path_resolved(self) -> Path:
        return Path(self.storage_path).resolve()

    @property
    def chroma_path_resolved(self) -> Path:
        return Path(self.chroma_path).resolve()

    @property
    def sql_index_path_resolved(self) -> Path:
        return Path(self.sql_index_path).resolve()


settings = Settings()
