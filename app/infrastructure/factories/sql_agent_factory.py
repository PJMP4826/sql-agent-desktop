import logging
from app.application.agents.sql_agent.sql_agent import SQLAgent
from app.domain.services.table_classifier import TableClassifier
from app.application.ports.llm_port import LLMPort
from app.infrastructure.database.sql.sql_database_adapter import SQLDatabaseAdapter
from app.infrastructure.database.sql.connection_manager import ConnetionManager
from app.config.settings import Settings
from app.infrastructure.websocket.websocket_client import WebSocketClient
from app.infrastructure.services.rag_client_service import RagClientService
from app.config.settings import Settings
from app.config.api_endpoints import ApiEndpoints
from app.infrastructure.services.json_to_toon import JSONtoTOON
from app.infrastructure.llm.runners.function_agent_runner import FunctionAgentRunner
from app.application.agents.sql_agent.prompts.sql_agent_prompts import SQLAgentPrompts

#agent tools

from app.infrastructure.llm.tools.sql_query_tool import SQLQueryTool
from app.infrastructure.llm.tools.get_context_conversation import GetContextConversation

from app.infrastructure.llm.tools.function_tools.current_date_time_tool import (
    create_current_date_time
)
from app.infrastructure.llm.tools.function_tools.generate_excel_function_tool import (
    create_generate_excel_function_tool
)

from app.infrastructure.llm.tools.function_tools.get_context_function_tool import (
    create_get_context_function_tool
)

from app.infrastructure.llm.tools.function_tools.sql_function_tool import (
    create_sql_query_function_tool
)

from llama_index.core.tools import FunctionTool




logger = logging.getLogger(__name__)


class SQLAgentFactory:
    """
    Factory para crear SQLAgent completamente configurado
    """
    
    def __init__(
        self,
        llm_client: LLMPort,
    ):
        self.llm_client = llm_client

    def create_tools(self, sql_query_tool: SQLQueryTool, get_context_tool: GetContextConversation) -> list[FunctionTool]:
        tools: list[FunctionTool] = []

        sql_tool = create_sql_query_function_tool(sql_query_tool)
        date_time_tool = create_current_date_time()
        get_context_conversation_tool = create_get_context_function_tool(get_context_tool)
        generate_excel_report = create_generate_excel_function_tool(self.llm_client)

        tools.append(sql_tool)
        tools.append(date_time_tool)
        tools.append(get_context_conversation_tool)
        tools.append(generate_excel_report)

        return tools
    
    def create_sql_agent(self, settings: Settings, agent_name: str = "Asistente Contable") -> SQLAgent:
        """
        Crear SQLAgent con todas sus dependencias.
        
        Args:
            agent_name: Nombre del agente
            
        Returns:
            SQLAgent completamente configurado
        """
        try:
            logger.info("Creating SQL Agent with dependencies...")
            
            # Crear herramientas
            table_classifier = TableClassifier()
            # context_builder = ContextBuilder(rag_service=general_rag)
            
            connection_manager = ConnetionManager(settings=settings)

            sql_adapter = SQLDatabaseAdapter(connection_manager=connection_manager)

            api = ApiEndpoints(settings)
            ws = WebSocketClient(api.chat.get_sql_context)
            print(f"URL: {api.chat.get_sql_context}")

            rag_service = RagClientService(ws_client=ws)

            converter_json_to_toon = JSONtoTOON()

            # Crear SQL Query Tool
            sql_query_tool = SQLQueryTool(
                llm_client=self.llm_client,
                connection_manager=connection_manager,
                sql_adapter=sql_adapter,
                rag_service=rag_service,
                table_classifier=table_classifier,
                converter=converter_json_to_toon
            )

            get_context_tool = GetContextConversation(
                rag_service=rag_service
            )

            tools = self.create_tools(
                sql_query_tool=sql_query_tool,
                get_context_tool=get_context_tool
            )

            runner = FunctionAgentRunner(
                llm_client=self.llm_client,
                tools=tools
            )
            
            # Crear SQL Agent
            sql_agent = SQLAgent(
                runner=runner,
                agent_name=agent_name,
                system_prompt=SQLAgentPrompts.get_prompt()
            )
            
            logger.info(f"SQL Agent '{agent_name}' created successfully")
            return sql_agent
            
        except Exception as e:
            logger.exception(f"Error creating SQL Agent: {e}")
            raise