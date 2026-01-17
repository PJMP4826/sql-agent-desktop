from typing import Any
from dataclasses import dataclass, asdict
from app.infrastructure.adapters.llamaindex_tool_result import LlamaIndexToolResultAdapter


@dataclass
class ToolResultEvent:
    """para resultados de herramientas"""

    tool_name: str
    tool_output: LlamaIndexToolResultAdapter
    success: bool = True
    error_message: str | None = None

    def __str__(self) -> str:
        output_str = str(self.tool_output)
        if len(output_str) > 500:
            output_str = output_str[:500] + " ..."
        status = "ok" if self.success else "failed"
        return f"{status} - {self.tool_name}: {output_str}"

    def to_dict(self) -> dict[str, Any]:
        """Convierte a diccionario"""
        return asdict(self)
