from typing import Optional
from abc import ABC, abstractmethod
from tool import Tool


class Agent(ABC):

    def __init__(self, name: str, tools: Optional[list[Tool]] = None):
        self.name = name
        self.tools = tools or []

    @abstractmethod
    async def chat(self):
        raise NotImplementedError

    def add_tool(self, tool: Tool):
        self.tools.append(tool)
