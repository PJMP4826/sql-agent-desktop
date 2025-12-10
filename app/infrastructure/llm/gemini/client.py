from typing import AsyncGenerator, Generator
from llama_index.core.llms.llm import LLM
from app.application.ports.llm_port import LLMPort
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.core.base.llms.types import CompletionResponse
from llama_index.core.base.embeddings.base import BaseEmbedding
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding # type: ignore

class GeminiAdapter(LLMPort):

    def __init__(
        self, llm_model_name: str, api_key: str, embed_model: str = "text-embedding-004"
    ) -> None:
        self.llm_model_name: str = llm_model_name
        self.llm: LLM = GoogleGenAI(model=llm_model_name, api_key=api_key)
        self.embed_model: BaseEmbedding = GoogleGenAIEmbedding(model_name=embed_model, api_key=api_key)

    def generate_response(self, prompt: str) -> str:
        response = self.llm.complete(prompt)
        return response.text
    
    def generate_response_stream(self, prompt: str) -> Generator[CompletionResponse, None, None]:
        return self.llm.stream_complete(prompt)
    
    async def generate_async_response_stream(self, prompt: str) -> AsyncGenerator[CompletionResponse, None]:
        return await self.llm.astream_complete(prompt)

    def get_embed_model(self) -> BaseEmbedding:
        return self.embed_model

    def get_llm_model(self)-> LLM:
        return self.llm

    def get_llm_model_name(self) -> str:
        return self.llm_model_name
