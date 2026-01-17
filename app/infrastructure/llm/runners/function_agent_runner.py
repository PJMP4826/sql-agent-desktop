from app.application.ports.agent_runner_port import AgentRunnerPort
from app.application.dto.agent_execution_result import AgentExecutionResult
from app.application.ports.llm_port import LLMPort
from app.infrastructure.llm.context.agent_context import AgentContext


from llama_index.core.agent import FunctionAgent, ToolCall, ToolCallResult
from llama_index.core.agent import ToolCall, ToolCallResult
from llama_index.core.tools import FunctionTool
from app.domain.value_objects.tool_call_event import ToolCallEvent
from app.domain.value_objects.tool_result_event import ToolResultEvent
from app.infrastructure.adapters.llamaindex_tool_result import LlamaIndexToolResultAdapter

class FunctionAgentRunner(AgentRunnerPort):

    def __init__(
        self,
        llm_client: LLMPort,
        tools: list[FunctionTool],
    ):
        self.llm_client = llm_client
        self.tools = tools
        self._context: AgentContext | None = None

    def _get_or_create_context(self, agent: FunctionAgent) -> AgentContext:
        if self._context is None:
            self._context = AgentContext(agent)
        return self._context

    async def run(
        self,
        agent_name: str,
        system_prompt: str,
        user_input: str,
    ) -> AgentExecutionResult:
        try:
            agent = FunctionAgent(
                name=agent_name,
                llm=self.llm_client.get_llm_model(),
                tools=self.tools,
                system_prompt=system_prompt,
            )

            agent_context = self._get_or_create_context(agent=agent)

            tool_results: list[ToolResultEvent] = []
            tool_calls: list[ToolCallEvent] = []

            handler = agent.run(user_msg=user_input, ctx=agent_context.context)

            async for event in handler.stream_events():
                if isinstance(event, ToolCall):
                    tool_call_event = ToolCallEvent(
                        tool_name=event.tool_name,
                        tool_kwargs=event.tool_kwargs # type: ignore
                    )

                    tool_calls.append(tool_call_event)
                elif isinstance(event, ToolCallResult):
                    tool_result = LlamaIndexToolResultAdapter(
                        tool_output=event.tool_output
                    )

                    tool_result_event = ToolResultEvent(
                        tool_name=event.tool_name,
                        tool_output=tool_result,
                        success=True
                    )

                    tool_results.append(tool_result_event)


            final_response = await handler # type: ignore

            return AgentExecutionResult(
                response_text=final_response, # type: ignore
                tool_calls=tool_calls,
                tool_results=tool_results,
                success=True,
            )

        except Exception as exc:
            return AgentExecutionResult(
                response_text="",
                tool_calls=[],
                tool_results=[],
                success=False,
                error_message=str(exc),
            )
