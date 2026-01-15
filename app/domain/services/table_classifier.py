import logging
from app.shared.constants.known_tables import filter_valid_tables
from app.shared.domain_exceptions import DomainException

logger = logging.getLogger(__name__)


class TableClassifier:
    def __init__(self) -> None:
        pass

    def inferir_tables(self, inferred_tables: list[str]) -> list[str]:
        """
        Inferir las tablas son relevantes para una consulta


        Args:
            inferred_tables: Consulta del usuario

        Returns:
            Lista de nombres de tablas relevantes

        Raises:
            DomainException: Si hay error en la inferencia
        """
        try:
            valid_tables: list[str] = filter_valid_tables(inferred_tables)

            logger.info(f"Tablas inferidas validas: {valid_tables}")

            if not valid_tables:
                logger.warning(
                    "No se encontraron tablas validas",
                    f"Inferidas: {inferred_tables}, Validas: {valid_tables}",
                )

            return valid_tables
        except Exception as e:
            logger.error(f"Error inferiendo tablas: {str(e)}")
            raise DomainException(
                "Error Validando tablas",
                details={"inferred_tables": inferred_tables, "error": str(e)},
            )