from typing import Any
from pydantic import BaseModel

class ExcelSheet(BaseModel):
    name: str
    headers: list[str]
    rows: list[list[Any]]