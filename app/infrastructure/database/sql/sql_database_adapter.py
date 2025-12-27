from typing import Optional
from llama_index.core import SQLDatabase
from sqlalchemy import inspect
from app.infrastructure.database.sql.connection_manager import ConnetionManager
from app.shared.infrastructure_exceptions import InfrastructureException


class SQLDatabaseAdapter:
    def __init__(self, connection_manager: ConnetionManager) -> None:
        self.connection_manager = connection_manager
        self._sql_database: Optional[SQLDatabase] = None

    def create_sql_database(self, include_tables: list[str]) -> SQLDatabase:
        try:
            sql_database = SQLDatabase(
                self.connection_manager.get_engine(),
                include_tables=include_tables,
            )

            return sql_database
        except Exception as e:
            raise InfrastructureException(
                f"Error al crear SQL Database: {str(e)}",
                details={"tables": include_tables, "error": str(e)},
            )

    def get_tables_disponibles(self) -> list[str]:
        """obtener lista de tablas disponibles"""
        try:
            engine = self.connection_manager.get_engine()
            inspector = inspect(engine)
            return inspector.get_table_names()
        except Exception as e:
            print(f"Error: {e}")
            return []
