from llama_index.core.tools import FunctionTool
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.core.workflow import Context
from app.domain.agents.sql_agent.prompts.sql_agent_prompts import SQLAgentPrompts
from app.application.ports.llm_port import LLMPort
from app.shared.domain_exceptions import AgentException
from app.domain.agents.sql_agent.tools.sql_query_tool import SQLQueryTool
from app.domain.agents.sql_agent.tools.function_tools.sql_function_tool import create_sql_query_function_tool


class SQLAgent:
    def __init__(
        self,
        llm_client: LLMPort,
        sql_query_tool: SQLQueryTool,
    ) -> None:
        self.agent_name: str = "Asistente Contable"
        self.llm_client = llm_client.get_llm_model()
        self.sql_query_tool = sql_query_tool

        self.system_prompt = SQLAgentPrompts.get_prompt()


        self.tools: list[FunctionTool] | None = self._create_tools()

        self._agent: FunctionAgent | None = None
        self._context_chat_history: Context | None = None
    
    def _create_tools(self) -> list[FunctionTool] | None:
        tools: list[FunctionTool] = []

        sql_tool = create_sql_query_function_tool(self.sql_query_tool)

        return tools.append(sql_tool)


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
            llm=self.llm_client,
            tools=self.tools,
            system_prompt=self.system_prompt,
        )

        return agent

    def create_context_chat_history(self) -> Context:
        return Context(self.agent)

    def chat(self, user_input: str) -> str:
        try:
            response = self.agent.run(user_msg=user_input)

            return str(response)
        except Exception as e:
            raise AgentException(
                "Error preguntando al SQL Agent",
                agent_name=self.agent_name,
                details={"user_input": user_input, "error": str(e)},
            )
