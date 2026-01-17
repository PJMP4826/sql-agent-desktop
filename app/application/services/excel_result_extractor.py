from typing import Any

from app.application.dto.chat_response import ChatResponse
from app.application.dto.excel_file_result import ExcelFileResult


class ExcelResultExtractor:
    EXCEL_TOOL_NAME = "generate_excel_report"

    def get_excel_file(self, response: ChatResponse) -> ExcelFileResult:
        """
        Obtiene un ExcelFileResult desde un ChatResponse.

        Raises ValueError if no Excel result is found or if the payload is invalid
        """
        for tool_result in response.tool_results:
            if self._is_excel_tool(tool_result):
                payload = tool_result.tool_output.get_payload()
                return self._build_excel_result(payload)

        raise ValueError("No Excel file found in tool results")

    def has_excel(self, response: ChatResponse) -> bool:
        return any(self._is_excel_tool(tr) for tr in response.tool_results)

    def _is_excel_tool(self, tool_result: Any) -> bool:
        return getattr(tool_result, "tool_name", None) == self.EXCEL_TOOL_NAME

    
    def _build_excel_result(self, data: dict[str, Any]) -> ExcelFileResult:
        return ExcelFileResult(
            type=data.get("type", "excel_file"),
            filename=data.get("filename", "reporte.xlsx"),
            content=data.get("content", ""),
            mime_type=data.get(
                "mime_type",
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            ),
            size_bytes=data.get("size_bytes", 0),
            sheets_count=data.get("sheets_count", 1),
            message=data.get("message", ""),
        )
