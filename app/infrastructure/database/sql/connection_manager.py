import logging
from sqlalchemy import create_engine, Engine, text
from app.shared.infrastructure_exceptions import InfrastructureException
from app.config.settings import Settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ConnetionManager:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self._engine: Engine | None = None

    def get_engine(self) -> Engine:
        if self._engine is None:
            self._engine = self._create_engine()
        return self._engine

    def _create_engine(self) -> Engine:
        try:

            connection_url = self.settings.database_url
            logger.info(
                f"Creando connection a BD {self.settings.db_name} en {self.settings.db_host}"
            )

            engine = create_engine(
                connection_url,
                echo=False,  # no mostrar SQL en logs
                pool_pre_ping=True,  # verificar connection antes de usar
                pool_recycle=3600,  # reciclar connections cada hora
                pool_size=5,  # size del pool
                max_overflow=10,  # connections extra permitidas
                pool_timeout=30,  # timeout para conectar
            )

            logger.info("Connection a base de datos exitosa")
            return engine

        except Exception as e:
            raise InfrastructureException(
                "No se ha establecido connection a SQL Server",
                details={
                    "db_name": self.settings.db_name,
                    "db_host": self.settings.db_host,
                    "error": str(e),
                },
            )

    def test_connection(self) -> dict[str, str | None]:
        try:
            engine = self.get_engine()
            with engine.connect() as conn:
                result = conn.execute(text("SELECT @@VERSION"))
                version = result.fetchone()[0] # type: ignore

                version_clean = version.split("\n")[0].strip() # type: ignore

                return {
                    "status": "success",
                    "version": version_clean,
                    "db_name": self.settings.db_name,
                }
        except Exception as e:
            #logger.error(f"Connection test failed: {e}")
            return {"status": "error", "message": str(e), "version": None}

    def close(self):
        if self._engine:
            self._engine.dispose()
            self._engine = None
            logger.info("SQL engine closed")
