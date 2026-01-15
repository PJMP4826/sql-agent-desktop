import logging
from app.domain.agents.sql_agent.sql_agent import SQLAgent
from app.domain.agents.sql_agent.tools.sql_query_tool import SQLQueryTool
from app.domain.services.table_classifier import TableClassifier
from app.application.ports.llm_port import LLMPort
from app.infrastructure.database.sql.sql_database_adapter import SQLDatabaseAdapter
from app.infrastructure.database.sql.connection_manager import ConnetionManager
from app.config.settings import Settings
from app.infrastructure.websocket.websocket_client import WebSocketClient
from app.infrastructure.services.rag_client_service import RagClientService
from app.config.settings import Settings
from app.config.api_endpoints import ApiEndpoints

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

            # Crear SQL Query Tool
            sql_query_tool = SQLQueryTool(
                llm_client=self.llm_client,
                connection_manager=connection_manager,
                sql_adapter=sql_adapter,
                rag_service=rag_service,
                table_classifier=table_classifier
            )

            # get_context_tool = GetContextConversation(
            #     rag_service=rag_service
            # )
            
            # Crear SQL Agent
            sql_agent = SQLAgent(
                llm_client=self.llm_client,
                sql_query_tool=sql_query_tool,
                # get_context_tool=get_context_tool,
                agent_name=agent_name
            )
            
            logger.info(f"SQL Agent '{agent_name}' created successfully")
            return sql_agent
            
        except Exception as e:
            logger.exception(f"Error creating SQL Agent: {e}")
            raise