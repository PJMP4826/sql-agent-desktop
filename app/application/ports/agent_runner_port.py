from abc import ABC
from app.application.dto.agent_execution_result import AgentExecutionResult

class AgentRunnerPort(ABC):
    async def run(
        self,
        agent_name: str,
        system_prompt: str,
        user_input: str,
    ) -> AgentExecutionResult:
        raise NotImplementedError
        

