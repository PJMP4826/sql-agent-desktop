from app.config.settings import Settings
from app.config.endpoints.chat_endpoints import ChatEndpoints

class ApiEndpoints:
    def __init__(self, settings: Settings) -> None:
        self.http_base_url: str = ""
        self.ws_base_url: str = settings.rag_client_base_url
        self.chat = ChatEndpoints(self.ws_base_url)


