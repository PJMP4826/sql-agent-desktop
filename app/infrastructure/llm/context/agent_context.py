from llama_index.core.workflow import Context
from llama_index.core.agent import FunctionAgent


class AgentContext:
    """
    Contexto para un Agent LLM de LlamaIndex
    """

    def __init__(self, agent: FunctionAgent):
        self._context = Context(agent)

    @property
    def context(self) -> Context | None:
        return self._context

    def reset(self) -> None:
        """
        Limpiar conversation history / memory
        """
        self._context = None
