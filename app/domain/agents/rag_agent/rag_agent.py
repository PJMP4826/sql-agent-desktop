from app.application.ports.vector_store_port import VectorStorePort
from app.application.ports.llm_port import LLMPort
from app.domain.agents.rag_agent.prompts.system_prompts import RagPrompts
from app.domain.agents.base.agent import Agent
from app.domain.services.rag_service import RagService
from app.shared.domain_exceptions import DomainException
from typing import Dict, Any


class RagAgent(Agent):
    def __init__(
        self, vector_store: VectorStorePort, llm_client: LLMPort, agent_type: str
    ) -> None:
        self.vector_store = vector_store
        self.llm_client = llm_client
        self.system_prompt = RagPrompts.get_prompt(agent_type)

        self.rag_service = RagService(
            vector_store=vector_store,
            llm_client=llm_client,
            system_prompt=self.system_prompt,
        )

    def ask(self, question: str, mode: str = "chat") -> str:
        try:
            if not mode == "chat":
                response: str = self.rag_service.query(question)

            response: str = self.rag_service.chat(question)

            return response
        except Exception as e:
            raise DomainException(
                "Error al procesar solicitud RAG",
                details={"question": question, "error": str(e)},
            )

    def add_knowledge(self, source: str, source_type: str = "file") -> Dict[str, Any]:
        try:
            if source_type == "directory":
                result = self.rag_service.index_directory(source)
            elif source_type == "file":
                result = self.rag_service.add_document(source)
            else:
                raise ValueError(f"Invalid source_type: {source_type}")

            return result

        except Exception as e:
            raise DomainException(
                "Error agregando conocimiento a agent",
                details={"source": source, "error": str(e)},
            )
