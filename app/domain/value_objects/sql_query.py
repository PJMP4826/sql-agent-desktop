from dataclasses import dataclass

@dataclass(frozen=True)
class SQLQuery:
    raw_sql: str
    tables_used: list[str]

    def __post_init__(self):
        if not self.raw_sql.strip().lower().startswith("select", "with"):
            raise ValueError("SQL debe ser una consulta SELECT valida")