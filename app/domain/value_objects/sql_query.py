from dataclasses import dataclass

@dataclass
class SQLQuery:
    sql_query: str
    response: str
