from google import genai
from google.genai import types
from typing import AsyncGenerator, Generator
from llama_index.core.llms.llm import LLM
from app.application.ports.llm_port import LLMPort
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.core.base.llms.types import CompletionResponse
from llama_index.core.base.embeddings.base import BaseEmbedding
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding # type: ignore
from app.domain.schemas.excel_report_schema import ExcelReport
from llama_index.core import Settings
from app.domain.services.token_counter import TokenCounter


class GeminiAdapter(LLMPort):

    def __init__(
        self, llm_model_name: str, api_key: str, embed_model: str, token_counter: TokenCounter
    ) -> None:
        self.token_counter = token_counter
        self.callback_manager = self.token_counter.callback_manager
        self.llm_model_name: str = llm_model_name
        self.llm: LLM = GoogleGenAI(
            model=llm_model_name, 
            api_key=api_key,
            callback_manager=self.callback_manager
        )
        self.embed_model: BaseEmbedding = GoogleGenAIEmbedding(model_name=embed_model, api_key=api_key)
        Settings.llm = self.llm
        Settings.embed_model = self.embed_model

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
    
    def generate_content(self, prompt: str) -> str:
        genai_client = genai.Client()

        model = genai_client.models.generate_content(
            model=self.llm_model_name,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=ExcelReport.model_json_schema()
            )
        )

        response = str(model.text)
        return response
    
    def get_token_counter(self) -> TokenCounter:
        return self.token_counter
    
        
