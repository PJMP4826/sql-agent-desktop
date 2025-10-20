import warnings
from src.api.routes import websocket_routes
from src.middlewares.cors import add_cors_middleware
from fastapi import FastAPI

warnings.filterwarnings("ignore", category=UserWarning)

app = FastAPI(
    title="AI Chat API",
    docs_url="/docs",
    description="ChatBot de servicio al cliente con base de conocimiento",
    version="1.0.0",
)

add_cors_middleware(app)

#webSocket
app.include_router(websocket_routes.router)
