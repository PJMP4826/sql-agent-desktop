import logging
from app.domain.agents.sql_agent.sql_agent import SQLAgent
from app.domain.agents.sql_agent.tools.sql_query_tool import SQLQueryTool
from app.domain.agents.sql_agent.tools.get_context_conversation import GetContextConversation
from app.domain.services.context_builder import ContextBuilder
from app.domain.services.table_classifier import TableClassifier
from app.domain.factories.rag_factory import RagServiceFactory
from app.application.ports.llm_port import LLMPort
from app.application.ports.vector_store_port import VectorStorePort
from app.infrastructure.database.sql.sql_database_adapter import SQLDatabaseAdapter
from app.infrastructure.database.sql.connection_manager import ConnetionManager
from app.config.settings import Settings

logger = logging.getLogger(__name__)


class SQLAgentFactory:
    """
    Factory para crear SQLAgent completamente configurado
    """
    
    def __init__(
        self,
        llm_client: LLMPort,
        vector_store: VectorStorePort
    ):
        self.llm_client = llm_client
        self.vector_store = vector_store
    
    def create_sql_agent(self, agent_name: str = "Asistente Contable") -> SQLAgent:
        """
        Crear SQLAgent con todas sus dependencias.
        
        Args:
            agent_name: Nombre del agente
            
        Returns:
            SQLAgent completamente configurado
        """
        try:
            logger.info("Creating SQL Agent with dependencies...")
            
            # 1. Crear RAG Factory
            rag_factory = RagServiceFactory(
                vector_store=self.vector_store,
                llm_client=self.llm_client
            )
            
            # 2. Crear RAG services para clasificación y contexto
            classifier_rag = rag_factory.create_classifier_rag()
            general_rag = rag_factory.create_general_rag()
            
            # 3. Crear herramientas
            table_classifier = TableClassifier(rag_service=classifier_rag)
            context_builder = ContextBuilder(rag_service=general_rag)
            
            settings = Settings() # type: ignore

            connection_manager = ConnetionManager(settings=settings)

            sql_adapter = SQLDatabaseAdapter(connection_manager=connection_manager)

            # 4. Crear SQL Query Tool
            sql_query_tool = SQLQueryTool(
                context_builder=context_builder,
                table_classifier=table_classifier,
                rag_factory=rag_factory,
                llm_client=self.llm_client,
                connection_manager=connection_manager,
                sql_adapter=sql_adapter
            )

            get_context_tool = GetContextConversation(
                rag_service=general_rag
            )
            
            # 5. Crear SQL Agent
            sql_agent = SQLAgent(
                llm_client=self.llm_client,
                sql_query_tool=sql_query_tool,
                get_context_tool=get_context_tool,
                agent_name=agent_name
            )
            
            logger.info(f"SQL Agent '{agent_name}' created successfully")
            return sql_agent
            
        except Exception as e:
            logger.exception(f"Error creating SQL Agent: {e}")
            raise