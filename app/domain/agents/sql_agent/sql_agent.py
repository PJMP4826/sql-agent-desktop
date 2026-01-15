from llama_index.core.tools import FunctionTool
from llama_index.core.agent.workflow import FunctionAgent, ToolCall, ToolCallResult
from llama_index.core.agent import ToolCall, ToolCallResult
from llama_index.core.workflow import Context
from app.domain.agents.sql_agent.prompts.sql_agent_prompts import SQLAgentPrompts
from app.application.ports.llm_port import LLMPort
from app.domain.agents.sql_agent.tools.sql_query_tool import SQLQueryTool
from app.domain.agents.sql_agent.tools.get_context_conversation import GetContextConversation
from app.domain.agents.sql_agent.tools.function_tools.sql_function_tool import create_sql_query_function_tool
from app.domain.agents.sql_agent.tools.function_tools.current_date_time_tool import create_current_date_time
from app.domain.agents.sql_agent.tools.function_tools.get_context_function_tool import create_get_context_function_tool
from app.domain.agents.sql_agent.tools.function_tools.generate_excel_function_tool import create_generate_excel_function_tool
from app.domain.value_objects.tool_call_event import ToolCallEvent
from app.domain.value_objects.tool_result_event import ToolResultEvent
from app.domain.value_objects.chat_response import ChatResponse
from app.domain.services.token_counter import TokenCounter


class SQLAgent:
    def __init__(
        self,
        llm_client: LLMPort,
        sql_query_tool: SQLQueryTool,
        # get_context_tool: GetContextConversation,
        agent_name: str
    ) -> None:
        self.agent_name: str = agent_name
        self.llm_client = llm_client
        self.sql_query_tool = sql_query_tool
        # self.get_context_tool = get_context_tool

        self.system_prompt = SQLAgentPrompts.get_prompt()


        self.tools: list[FunctionTool] | None = self._create_tools()

        self._agent: FunctionAgent | None = None
        self._context_chat_history: Context | None = None
    
    def _create_tools(self) -> list[FunctionTool]:
        tools: list[FunctionTool] = []

        sql_tool = create_sql_query_function_tool(self.sql_query_tool)
        date_time_tool = create_current_date_time()
        # get_context_conversation_tool = create_get_context_function_tool(self.get_context_tool)
        generate_excel_report = create_generate_excel_function_tool(self.llm_client)

        tools.append(sql_tool)
        tools.append(date_time_tool)
        # tools.append(get_context_conversation_tool)
        tools.append(generate_excel_report)

        return tools


    @property
    def agent(self):
        if self._agent is None:
            self._agent = self._create_agent()
        return self._agent

    @property
    def context_chat_history(self):
        if self._context_chat_history is None:
            self._context_chat_history = Context(self.agent)
        return self._context_chat_history

    def _create_agent(self) -> FunctionAgent:
        agent = FunctionAgent(
            name=self.agent_name,
            llm=self.llm_client.get_llm_model(),
            tools=self.tools,
            system_prompt=self.system_prompt,
        )

        return agent

    def create_context_chat_history(self) -> Context:
        return Context(self.agent)

    async def chat(self, user_input: str) -> ChatResponse:
        try:
            tool_results = []
            tool_results: list[ToolResultEvent] = []
            tool_calls: list[ToolCallEvent] = []

            handler = self.agent.run(user_msg=user_input, ctx=self.context_chat_history)

            async for event in handler.stream_events():
                if isinstance(event, ToolCall):
                    tool_call_event = ToolCallEvent(
                        tool_name=event.tool_name,
                        tool_kwargs=event.tool_kwargs # type: ignore
                    )

                    tool_calls.append(tool_call_event)
                elif isinstance(event, ToolCallResult):
                    tool_result_event = ToolResultEvent(
                        tool_name=event.tool_name,
                        tool_output=event.tool_output,
                        success=True
                    )

                    tool_results.append(tool_result_event)


            final_response = await handler # type: ignore
            
            # print("Tool results: ", tool_result_event.to_dict())
            return ChatResponse(
                tool_calls=tool_calls,
                tool_results=tool_results,
                response_text=final_response, # type: ignore
                success=True
            )
        except Exception as e:
            # ChatResponse con error
            return ChatResponse(
                response_text=f"Error: {str(e)}",
                success=False,
                error_message=str(e)
            )
        
    def get_token_counter(self) -> TokenCounter:
        return self.llm_client.get_token_counter()
