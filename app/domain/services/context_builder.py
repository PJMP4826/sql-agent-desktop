import logging
from app.domain.services.rag_service import RagService
from app.domain.agents.rag_agent.prompts.task_prompts import TaskPrompts
from app.domain.value_objects.table_relationship_maper import TableRelationshipMap
from app.shared.domain_exceptions import DomainException

logger = logging.getLogger(__name__)


class ContextBuilder:
    def __init__(self, rag_service: RagService) -> None:
        self.rag_service = rag_service

    def build_context(self, user_query: str, selected_tables: list[str]) -> str:

        try:
            basic_context: str = self._get_basic_context(
                user_query=user_query, tables=selected_tables
            )

            relationships: str = self._get_relationships(tables=selected_tables)

            full_context = self._combine_context(
                basic_context=basic_context,
                relationships=relationships,
                tables=selected_tables,
            )

            return full_context
        except Exception as e:
            raise DomainException(
                "Error creando el contexto SQL",
                details={
                    "user_query": user_query,
                    "tables": selected_tables,
                    "error": str(e),
                },
            )

    def _get_basic_context(self, user_query: str, tables: list[str]) -> str:
        prompt: str = TaskPrompts.format_basic_table_context(
            user_query=user_query, tables_relavantes=tables
        )

        try:
            response = self.rag_service.chat(prompt)
            return response.strip()
        except Exception as e:
            logging.error(
                f"Error obteniendo basic context: {str(e)} from ContextBuilder"
            )
            return "No se pudo obtener contexto básico de las tablas."

    def _get_relationships(self, tables: list[str]) -> str:
        relationships_list: list[str] = TableRelationshipMap.get_relationships_between(
            tables=tables
        )
        # concatenar la lista
        return "\n".join(relationships_list)

    def _combine_context(
        self, basic_context: str, relationships: str, tables: list[str]
    ) -> str:
        context: str = TaskPrompts.format_combine_context(
            tables_selected=tables,
            basic_context=basic_context,
            relationships=relationships,
        )

        return context.strip()
