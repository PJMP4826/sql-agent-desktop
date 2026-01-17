import json
import logging
from typing import Any
from app.domain.services.table_classifier import TableClassifier
from app.infrastructure.services.sql_query_service import SQLQueryService
from app.application.ports.llm_port import LLMPort
from app.infrastructure.database.sql.sql_database_adapter import SQLDatabaseAdapter
from app.infrastructure.database.sql.connection_manager import ConnetionManager
from app.shared.domain_exceptions import DomainException
from app.application.ports.rag_client_port import RagClientPort
from app.infrastructure.services.json_to_toon import JSONtoTOON

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SQLQueryTool:
    def __init__(
        self,
        rag_service: RagClientPort,
        llm_client: LLMPort,
        connection_manager: ConnetionManager,
        sql_adapter: SQLDatabaseAdapter,
        table_classifier: TableClassifier,
        converter: JSONtoTOON
    ) -> None:
        self._rag_service = rag_service
        self.llm_client = llm_client
        self.connection_manager = connection_manager
        self.sql_adapter = sql_adapter
        self.table_classifier = table_classifier
        self._converter = converter

    def execute_nl_query(self, query: str, verbose: bool = False) -> str:
        try:
            rag_response = self._get_context_rag(query=query)

            include_tables = self._parse_includes_tables(rag_response=rag_response)

            if not include_tables:
                logger.error("No se pudieron identificar tablas relevantes")

            business_context = self._builder_context(rag_response=rag_response)

            # consulatar a la db usando lenguaje natural
            sql_query_service = self._create_sql_service(
                include_tables=include_tables,
                business_context=business_context,
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

    def _parse_includes_tables(self, rag_response: dict[str, Any]) -> list[str]:
        try:
            result_inferred_tables = rag_response.get("content").get("inferred_tables")  # type: ignore
            
            # parsear y validar tablas
            table_list = self.table_classifier.inferir_tables(result_inferred_tables)

            return table_list
        except Exception as e:
            raise DomainException(
                f"Error indentificando tables relevantes: {str(e)}",
            )

    def _builder_context(self, rag_response: dict[str, Any]) -> str:
        try:
            result_business_context = rag_response.get("content").get("business_context")  # type: ignore

            print(f"BUSINESS CONTEXT DICT: {result_business_context}")

            business_context_toon = self._dict_to_toon(result_business_context)

            return business_context_toon
        except Exception as e:
            raise DomainException(f"Error al crear context para el SQL Agent: {str(e)}")

    def _dict_to_toon(self, business_context: dict[str, Any]) -> str:
        try:
            toon_output = self._converter.convert(business_context)
            print(f"BUSINESS CONTEXT TOON: {toon_output}")
            return toon_output
        except Exception as e:
            raise DomainException(
                f"Error al convertir JSON a TOON: {str(e)}"
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
