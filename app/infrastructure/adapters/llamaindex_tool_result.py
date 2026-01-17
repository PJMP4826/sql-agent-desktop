# infrastructure/adapters/llamaindex_tool_result.py
import ast
from typing import Any
from llama_index.core.tools import ToolOutput

class LlamaIndexToolResultAdapter:
    def __init__(self, tool_output: ToolOutput):
        self._tool_output = tool_output
    

    def get_payload(self) -> dict[str, Any]:
        if hasattr(self._tool_output, "blocks") and self._tool_output.blocks:
            raw = self._tool_output.blocks[0].text # type: ignore
        else:
            raw = str(self._tool_output)

        if isinstance(raw, str):
            return ast.literal_eval(raw)

        raise ValueError("Invalid tool output payload")
