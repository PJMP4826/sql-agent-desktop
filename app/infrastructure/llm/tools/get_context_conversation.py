from app.shared.domain_exceptions import AgentException
from app.application.ports.rag_client_port import RagClientPort

class GetContextConversation:
    def __init__(self, rag_service: RagClientPort) -> None:
        self.rag_service = rag_service


    def get_context(self, agent_question: str) -> str:
         try:
            context = self.rag_service.chat(agent_question)

            return context
         except Exception as e:
            raise AgentException(
                "Error al obtener contexto conversacional para Agent",
                details={
                    "error": str(e)
                }
            )

