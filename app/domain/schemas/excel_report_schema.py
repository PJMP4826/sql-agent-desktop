from app.domain.schemas.excel_sheet_schema import ExcelSheet
from pydantic import BaseModel

class ExcelReport(BaseModel):
    sheets: list[ExcelSheet]