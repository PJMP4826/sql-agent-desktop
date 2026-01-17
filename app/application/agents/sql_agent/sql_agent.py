from app.application.dto.chat_response import ChatResponse
from app.infrastructure.services.token_counter import TokenCounter
from app.infrastructure.llm.runners.function_agent_runner import FunctionAgentRunner


class SQLAgent:
    def __init__(
        self,
        runner: FunctionAgentRunner,
        agent_name: str,
        system_prompt: str
    ) -> None:
        self.agent_name: str = agent_name
        self._runner = runner
        self._system_prompt = system_prompt


    async def chat(self, user_input: str) -> ChatResponse:
        try:
           result = await self._runner.run(
               agent_name=self.agent_name,
               system_prompt=self._system_prompt,
               user_input=user_input
           )

           return ChatResponse(
                response_text=result.response_text,
                tool_calls=result.tool_calls,
                tool_results=result.tool_results,
                success=result.success,
                error_message=result.error_message,
           )
        except Exception as e:
            # ChatResponse con error
            return ChatResponse(
                response_text=f"Error: {str(e)}",
                success=False,
                error_message=str(e)
            )
        
    def get_token_counter(self) -> TokenCounter:
        return self._runner.llm_client.get_token_counter()
