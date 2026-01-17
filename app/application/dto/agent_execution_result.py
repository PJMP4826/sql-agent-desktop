from typing import Any
from dataclasses import dataclass

@dataclass
class AgentExecutionResult:
    response_text: str
    tool_calls: list[Any]
    tool_results: list[Any]
    success: bool
    error_message: str | None = None
