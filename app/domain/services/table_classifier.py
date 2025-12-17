import re
import json
import logging
from typing import Any
from app.domain.services.rag_service import RagService
from app.shared.constants.known_tables import filter_valid_tables
from app.shared.domain_exceptions import DomainException

logger = logging.getLogger(__name__)


class TableClassifier:
    def __init__(self, rag_service: RagService) -> None:
        self.rag_service = rag_service

    def inferir_tables(self, user_input: str) -> list[str]:
        """
        Inferir las tablas son relevantes para una consulta


        Args:
            user_input: Consulta del usuario

        Returns:
            Lista de nombres de tablas relevantes

        Raises:
            DomainException: Si hay error en la inferencia
        """
        try:
            if not user_input:
                logger.warning("User input is empty from inferir_tables()")

            response: str = self.rag_service.chat(user_input=user_input)
            logger.info(f"Tablas inferidas string: {response}")

            tables_parse = self._parse_response(response)

            valid_tables: list[str] = filter_valid_tables(tables_parse)

            logger.info(f"Tablas inferidas validas: {valid_tables}")

            if not valid_tables:
                logger.warning(
                    "No se encontraron tablas validas",
                    f"Inferidas: {tables_parse}, Validas: {valid_tables}",
                )

            return valid_tables
        except Exception as e:
            logger.error(f"Error inferiendo tablas: {str(e)}")
            raise DomainException(
                "Error inferiendo tablas",
                details={"user_input": user_input, "error": str(e)},
            )

    def _parse_response(self, response: str) -> list[str]:

        response_clean: str = response.strip()

        try:
            json_match = re.search(r"\[.*?\]", response_clean, re.DOTALL)

            if json_match:
                response_clean = json_match.group(0)

            tables_list: list[Any] = json.loads(response_clean)

            if not isinstance(tables_list, list):  # type: ignore
                print(f"Error: La respuesta no es una lista: {tables_list}")
                return []

            tables: list[str] = [t for t in tables_list if isinstance(t, str)]
            return tables

        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON response: {e}")
            logger.debug(f"Response was: {response[:500]}")
            return []
        except Exception as e:
            logger.exception(f"Error parsing response: {e}")
            return []
