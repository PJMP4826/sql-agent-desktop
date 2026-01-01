from llama_index.core.callbacks import CallbackManager, TokenCountingHandler
from llama_index.core import Settings


class TokenCounter:
    def __init__(
        self,
        token_counting_handler: TokenCountingHandler,
        callback_manager: CallbackManager,
    ) -> None:
        self.token_counting_handler = token_counting_handler
        self.callback_manager = callback_manager
        Settings.callback_manager = self.callback_manager

    def prompt_llm_token_count(self) -> int:
        return self.token_counting_handler.prompt_llm_token_count

    def completion_llm_token_count(self) -> int:
        return self.token_counting_handler.completion_llm_token_count

    def total_llm_token_count(self) -> int:
        return self.token_counting_handler.total_llm_token_count

    def total_embedding_token_count(self) -> int:
        return self.token_counting_handler.total_embedding_token_count
