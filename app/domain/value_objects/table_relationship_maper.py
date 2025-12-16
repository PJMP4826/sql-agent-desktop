from app.shared.constants.table_relationships import TABLE_RELATIONSHIPS
from typing import Optional


class TableRelationshipMap:

    # obtener relaciones entre un conjunto de tablas.
    # retorna lista de strings describiendo las relaciones
    @classmethod
    def get_relationships_between(cls, tables: list[str]) -> list[str]:

        relationships: list[str] = []

        for i, table1 in enumerate(tables):
            if table1 not in TABLE_RELATIONSHIPS:
                continue

            for table2 in tables[i + 1 :]:
                # relacion directa
                if table2 in TABLE_RELATIONSHIPS[table1]:
                    relationships.append(
                        f"{table1} <-> {table2}: {TABLE_RELATIONSHIPS[table1][table2]}"
                    )

                # relacion inversa
                elif (
                    table2 in TABLE_RELATIONSHIPS
                    and table1 in TABLE_RELATIONSHIPS[table2]
                ):
                    relationships.append(
                        f"- {table2} <-> {table1}: {TABLE_RELATIONSHIPS[table2][table1]}"
                    )

        if not relationships:
            return [
                "No se encontraron relaciones logicas directas documentadas entre estas tablas"
                "Considera usar subconsultas o consultas separadas"
            ]

        return relationships

    # obtener relacion directa entre una tabla y otra
    @classmethod
    def get_relationship(cls, from_table: str, to_table: str) -> Optional[str]:
        if from_table in TABLE_RELATIONSHIPS:
            if to_table in TABLE_RELATIONSHIPS[from_table]:
                return TABLE_RELATIONSHIPS[from_table][to_table]

        # intentar relacion inversa
        if to_table in TABLE_RELATIONSHIPS:
            if from_table in TABLE_RELATIONSHIPS[to_table]:
                return TABLE_RELATIONSHIPS[to_table][from_table]

        return "No hay relacion directa"
