from typing import Any
from dataclasses import dataclass, field
from app.domain.value_objects.tool_result_event import ToolResultEvent
from app.domain.value_objects.tool_call_event import ToolCallEvent

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

    
    def has_errors(self) -> bool:
        """verificar si hay errores"""
        if not self.success:
            return True
        return False
