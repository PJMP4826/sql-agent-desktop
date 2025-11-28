from dataclasses import dataclass, field
from typing import Optional
from sql_query import SQLQuery
from datetime import datetime

#representa la consulta del usuario
#y su traduccion a sql
@dataclass
class Query:
    id: int
    user_input: str = ""
    sql_query: Optional[SQLQuery] = None
    created_at: datetime = field(default=datetime.utcnow)