import ast
from typing import Any
from dataclasses import dataclass, field
from app.domain.value_objects.tool_result_event import ToolResultEvent
from app.domain.value_objects.tool_call_event import ToolCallEvent
from app.domain.value_objects.excel_file_result import ExcelFileResult
from llama_index.core.tools import ToolOutput

@dataclass
class ChatResponse:
    """
    Para respuesta completa del chat de Agent SQL
    """

    response_text: str
    tool_results: list[ToolResultEvent] = field(default_factory=list) # type: ignore
    tool_calls: list[ToolCallEvent] = field(default_factory=list) # type: ignore
    success: bool = True
    error_message: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "response_text": self.response_text,
            "tool_results": [r.to_dict() for r in self.tool_results],
            "tool_calls": [c.to_dict() for c in self.tool_calls],
            "success": self.success,
            "error_message": self.error_message,
        }

    def has_tool_results(self) -> bool:
        """Verifica si hay resultados de herramientas"""
        return len(self.tool_results) > 0

    def get_excel_files(self) -> ExcelFileResult:
        """
        extraer el archivo Excel de los tool results
        """
        for tool_result in self.tool_results:
            if tool_result.tool_name == "generate_excel_report":
                tool_output: ToolOutput = tool_result.tool_output

               # Obtener el contenido del block
                if hasattr(tool_output, 'blocks') and tool_output.blocks:
                    data = tool_output.blocks[0].text # type: ignore
                else:
                    data = str(tool_output) # type: ignore

                # Convertir a dict si es string
                if isinstance(data, str):
                    data: dict[str, Any] = ast.literal_eval(data)

                return ExcelFileResult(
                    type=data.get("type", "excel_file"),
                    filename=data.get("filename", "reporte.xlsx"),
                    content=data.get("content", ""),
                    mime_type=data.get("mime_type", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"),
                    size_bytes=data.get("size_bytes", 0),
                    sheets_count=data.get("sheets_count", 1),
                    message=data.get("message", "")
                )

        raise ValueError("No se encontró archivo Excel en los resultados")
    
        
    def has_excel_file(self) -> bool:
        for tool_result in self.tool_results:
            if tool_result.tool_name == "generate_excel_report":
               return True
        return False

    def has_errors(self) -> bool:
        """verificar si hay errores"""
        if not self.success:
            return True
        return False
