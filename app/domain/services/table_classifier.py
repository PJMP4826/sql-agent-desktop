import re
import json
import logging
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
            tables_list: list[str] = json.loads(response_clean)
            if isinstance(tables_list, list) and all(isinstance(t, str) for t in tables_list): # type: ignore
                return tables_list
        except Exception:
            pass

        json_match = re.search(r"\[.*?\]", response_clean, re.DOTALL)
        if json_match:
            try:
                tables_list = json.loads(json_match.group(0))
                if isinstance(tables_list, list) and all(isinstance(t, str) for t in tables_list): # type: ignore
                    return tables_list
            except Exception:
                pass

        matches = re.findall(r'`([^`]+)`', response_clean)
        if matches:
            return matches

        possible_lines = [line.strip() for line in response_clean.splitlines() if line.strip()]
        clean_lines: list[str] = []
        for line in possible_lines:
            line = re.sub(r'^[-*•]\s*', '', line)
            if len(line.split()) == 1 and len(line) < 60:
                clean_lines.append(line)
        if clean_lines:
            return clean_lines

        # split por coma
        if ',' in response_clean:
            posibles = [x.strip() for x in response_clean.split(',')]
            if all(len(x.split()) == 1 for x in posibles):
                return posibles

        # si nada funciona 
        logger.warning(f"No fue posible parsear tablas validas: {response[:200]}")
        return []
