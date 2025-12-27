from typing import Any
from dataclasses import dataclass, asdict


@dataclass
class ToolCallEvent:
    """dataclass para eventos de llamada a herramientas"""

    tool_name: str
    tool_kwargs: dict[str, Any]

    def __str__(self) -> str:
        kwargs_str = str(self.tool_kwargs)
        if len(kwargs_str) > 500:
            kwargs_str = kwargs_str[:500] + " ..."
        return f"{self.tool_name}({kwargs_str})"

    def to_dict(self) -> dict[str, Any]:
        """convierte a diccionario"""
        return asdict(self)
