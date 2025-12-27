from app.application.ports.llm_port import LLMPort
from app.infrastructure.database.sql.sql_database_adapter import SQLDatabaseAdapter
from app.infrastructure.database.sql.connection_manager import ConnetionManager
from app.infrastructure.llm.query_engines.nl_sql_engine_factory import (
    NLSQLEngineFactory,
)
from llama_index.core.query_engine import NLSQLTableQueryEngine
from app.shared.domain_exceptions import DomainException
from app.domain.value_objects.sql_query import SQLQuery


class SQLQueryService:
    def __init__(
        self,
        llm_client: LLMPort,
        connection_manager: ConnetionManager,
        sql_adapter: SQLDatabaseAdapter,
        include_tables: list[str],
        business_context: str,
        verbose_sql: bool = False,
    ) -> None:
        """
        Args:
            llm_client: Cliente LLM
            include_tables: Tablas a incluir en el engine
            business_context: Contexto de negocio opcional
            verbose_sql: Si mostrar SQL generado en logs
        """
        self.llm_client = llm_client
        self.include_tables = include_tables
        self.business_context = business_context
        self.verbose_sql = verbose_sql

        self.connection_manager = connection_manager
        self.sql_adapter = sql_adapter

        self._query_engine = None

    @property
    def query_engine(self):
        if self._query_engine is None:
            self._query_engine = self._create_query_engine()
        return self._query_engine

    def _create_query_engine(self) -> NLSQLTableQueryEngine:
        try:
            sql_database = self.sql_adapter.create_sql_database(
                include_tables=self.include_tables
            )

            query_engine = NLSQLEngineFactory.create_engine(
                sql_database=sql_database,
                llm_client=self.llm_client,
                tables=self.include_tables,
                business_context=self.business_context,
                synthesize_response=False,
                verbose=self.verbose_sql,
            )

            return query_engine
        except Exception as e:
            raise DomainException(
                f"Failed to initialize SQL query engine: {str(e)}",
                details={"tables": self.include_tables, "error": str(e)},
            )

    def query(self, user_query: str) -> SQLQuery:
        try:
            # ejecutar el sql y recuperar la respuesta
            response = self.query_engine.query(user_query)

            #sql_query = response.metadata["sql_query"]
            sql_query = getattr(response, "metadata", {}).get("sql_query", "N/A")

            return SQLQuery(sql_query=sql_query, response=str(response))
        except Exception as e:
            raise DomainException(
                f"Error al consultar el con NL Query Engine: {str(e)}",
                details={"user_query": user_query, "error": str(e)},
            )

    def test_connection(self) -> dict[str, str | None]:
        return self.connection_manager.test_connection()

    def close(self):
        self.connection_manager.close()
