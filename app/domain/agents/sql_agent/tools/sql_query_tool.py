import logging
from app.domain.services.context_builder import ContextBuilder
from app.domain.factories.rag_factory import RagServiceFactory
from app.domain.services.table_classifier import TableClassifier
from app.domain.services.sql_query_service import SQLQueryService
from app.application.ports.llm_port import LLMPort
from app.infrastructure.database.sql.sql_database_adapter import SQLDatabaseAdapter
from app.infrastructure.database.sql.connection_manager import ConnetionManager
from app.shared.domain_exceptions import DomainException


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SQLQueryTool:
    def __init__(
        self,
        context_builder: ContextBuilder,
        table_classifier: TableClassifier,
        rag_factory: RagServiceFactory,
        llm_client: LLMPort,
        connection_manager: ConnetionManager,
        sql_adapter: SQLDatabaseAdapter,
    ) -> None:
        self.context_builder = context_builder
        self.table_classifier = table_classifier
        self.rag_factory = rag_factory

        self.llm_client: LLMPort = llm_client
        self.connection_manager = connection_manager
        self.sql_adapter = sql_adapter

    def execute_nl_query(self, query: str, verbose: bool = False) -> str:
        try:
            include_tables = self._parse_includes_tables(user_input=query)

            if not include_tables:
                logger.error("No se pudieron identificar tablas relevantes")

            business_context = self._create_business_context(
                user_input=query, tables_list=include_tables
            )

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
                "Error ejecutand NL query",
                details={"success": False, "error": str(e), "user_input": query},
            )

    def _parse_includes_tables(self, user_input: str) -> list[str]:
        try:

            classifier_rag = self.rag_factory.create_classifier_rag()

            # obtener respuesta del rag con rol clasificador
            tables_inferidas = classifier_rag.chat(user_input)

            # parsear y validar tablas
            table_list = self.table_classifier.inferir_tables(tables_inferidas)

            return table_list
        except Exception as e:
            raise DomainException(
                "Error indentificando tables relevantes",
                details={"user_input": user_input, "error": str(e)},
            )

    def _create_business_context(self, user_input: str, tables_list: list[str]) -> str:
        try:
            business_context = self.context_builder.build_context(
                user_query=user_input, selected_tables=tables_list
            )

            return business_context
        except Exception as e:
            raise DomainException(
                "Error creando business context",
                details={
                    "user_input": user_input,
                    "tables": tables_list,
                    "error": str(e),
                },
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
