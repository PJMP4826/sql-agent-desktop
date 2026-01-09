class ChatEndpoints:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    @property
    def get_sql_context(self) -> str:
        return f"{self.base_url}/chat/ws"