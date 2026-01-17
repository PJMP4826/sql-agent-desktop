from abc import ABC, abstractmethod
from llama_index.core.llms.llm import LLM
from llama_index.core.base.embeddings.base import BaseEmbedding
from app.infrastructure.services.token_counter import TokenCounter


class LLMPort(ABC):
    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_embed_model(self) -> BaseEmbedding:
        raise NotImplementedError

    @abstractmethod
    def get_llm_model(self) -> LLM:
        raise NotImplementedError

    @abstractmethod
    def get_llm_model_name(self) -> str:
        raise NotImplementedError
    
    @abstractmethod
    def generate_content(self, prompt: str) -> str:
        raise NotImplementedError
    
    @abstractmethod
    def get_token_counter(self) -> TokenCounter:
        raise NotImplementedError
