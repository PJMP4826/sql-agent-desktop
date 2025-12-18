from typing import Optional
from llama_index.core.llms.llm import LLM
from app.application.ports.llm_port import LLMPort
from llama_index.core.base.embeddings.base import BaseEmbedding
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding  # type: ignore
from llama_index.llms.lmstudio import LMStudio  # type: ignore


class LmStudioAdapter(LLMPort):
    def __init__(self, llm_model_name: str, base_url: str,api_key: Optional[str], embed_model: str) -> None:
        self.llm_model_name: str = llm_model_name
        self.llm: LLM = LMStudio(
            model_name=self.llm_model_name,
            base_url=base_url,
            temperature=0.7,
        )
        self.embed_model: BaseEmbedding = GoogleGenAIEmbedding(
            model_name=embed_model, api_key=api_key
        )
    
    def generate_response(self, prompt: str) -> str:
        response = self.llm.complete(prompt)
        return response.text
    
    def get_embed_model(self) -> BaseEmbedding:
        return self.embed_model

    def get_llm_model(self)-> LLM:
        return self.llm

    def get_llm_model_name(self) -> str:
        return self.llm_model_name
