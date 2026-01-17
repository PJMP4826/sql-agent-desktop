from app.infrastructure.services.rag_service import RagService
from app.application.ports.vector_store_port import VectorStorePort
from app.application.ports.llm_port import LLMPort
from app.application.agents.rag_agent.prompts.system_prompts import RagPrompts

class RagServiceFactory:
    """
    Factory para crear instancias de RagService con diferentes configuraciones
    """
    
    def __init__(
        self,
        vector_store: VectorStorePort,
        llm_client: LLMPort
    ):
        self.vector_store = vector_store
        self.llm_client = llm_client
    
    def create_classifier_rag(self) -> RagService:
        """
        crear RagService configurado para clasificacion de tablas.
        """
        return RagService(
            vector_store=self.vector_store,
            llm_client=self.llm_client,
            system_prompt=RagPrompts.get_prompt("clasificador_tablas"),
            auto_index_on_empty=True
        )
    
    def create_general_rag(self) -> RagService:
        """
        crear RagService configurado para consultas generales.
        """
        return RagService(
            vector_store=self.vector_store,
            llm_client=self.llm_client,
            system_prompt=RagPrompts.get_prompt("general"),
            auto_index_on_empty=True
        )
    
    def create_conversational_rag(self) -> RagService:
        """
        crear RagService configurado para conversacion.
        """
        return RagService(
            vector_store=self.vector_store,
            llm_client=self.llm_client,
            system_prompt=RagPrompts.get_prompt("conversational"),
            auto_index_on_empty=True
        )