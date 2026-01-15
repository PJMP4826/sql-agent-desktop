import logging
import json
from app.domain.services.table_classifier import TableClassifier
from app.domain.services.sql_query_service import SQLQueryService
from app.application.ports.llm_port import LLMPort
from app.infrastructure.database.sql.sql_database_adapter import SQLDatabaseAdapter
from app.infrastructure.database.sql.connection_manager import ConnetionManager
from app.shared.domain_exceptions import DomainException
from app.application.ports.rag_client_port import RagClientPort
from typing import Any


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SQLQueryTool:
    def __init__(
        self,
        rag_service: RagClientPort,
        llm_client: LLMPort,
        connection_manager: ConnetionManager,
        sql_adapter: SQLDatabaseAdapter,
        table_classifier: TableClassifier
    ) -> None:
        self._rag_service = rag_service
        self.llm_client = llm_client
        self.connection_manager = connection_manager
        self.sql_adapter = sql_adapter
        self.table_classifier = table_classifier

    def execute_nl_query(self, query: str, verbose: bool = False) -> str:
        try:
            rag_response = self._get_context_rag(query=query)

            inferred_tables = rag_response.get("content").get("inferred_tables") # type: ignore

            include_tables = self._parse_includes_tables(inferred_tables=inferred_tables)

            if not include_tables:
                logger.error("No se pudieron identificar tablas relevantes")

            business_context = rag_response.get("content").get("business_context") # type: ignore
            
            print(f"BUSINESS CONTEXT: {business_context}")

            # consulatar a la db usando lenguaje natural
            sql_query_service = self._create_sql_service(
                include_tables=include_tables,
                business_context=str(business_context),
                verbose_sql=verbose,
            )

            result = sql_query_service.query(user_query=query)

            logger.info(f"SQL GENERADO: {result.sql_query}")

            return result.response
        except Exception as e:
            raise DomainException(
                f"Error ejecutand NL query: {str(e)}",
                details={"success": False, "error": str(e), "user_input": query},
            )
    
    def _get_context_rag(self, query: str) -> dict[str, Any]:
        try:
            response = self._rag_service.query(query=query)

            data = json.loads(response)

            return data
        except Exception as e:
            raise DomainException(
                f"Error obteniendo contexto desde el API RAG: {str(e)}"
            )

    def _parse_includes_tables(self, inferred_tables: list[str]) -> list[str]:
        try:

            # parsear y validar tablas
            table_list = self.table_classifier.inferir_tables(inferred_tables)

            return table_list
        except Exception as e:
            raise DomainException(
                "Error indentificando tables relevantes",
                details={"inferred_tables": inferred_tables, "error": str(e)},
            )


    def _create_sql_service(
        self,
        include_tables: list[str],
        business_context: str,
        verbose_sql: bool = False,
    ) -> SQLQueryService:
        return SQLQueryService(
            llm_client=self.llm_client,
            connection_manager=self.connection_manager,
            sql_adapter=self.sql_adapter,
            include_tables=include_tables,
            business_context=business_context,
            verbose_sql=verbose_sql,
        )
