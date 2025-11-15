# import warnings
# from src.api.routes import websocket_routes
# from src.api.routes import api_routes
# from src.middlewares.cors import add_cors_middleware
# from fastapi import FastAPI
import asyncio
from src.core.chat_query_engine import ChatQueryEngine
from src.api.presentation.websocket.agent_handler import AgentHandler
from src.cli.main import CLI

# warnings.filterwarnings("ignore", category=UserWarning)

# app = FastAPI(
#     title="AI Chat API",
#     docs_url="/docs",
#     description="ChatBot de servicio al cliente con base de conocimiento",
#     version="1.0.0",
# )

# add_cors_middleware(app)

# #webSocket
# app.include_router(websocket_routes.router)
# app.include_router(api_routes.router)

# chat_engine = ChatQueryEngine()
# chat_engine.run_chat()
async def main():
    try:
        agent_handler = AgentHandler()
        await agent_handler.run_chat()
    except Exception as e:
        print(f"\n Error fatal al inicializar: {str(e)}")


if __name__ == "__main__":
    asyncio.run(main())


# if __name__ == "__main__":

#     try:
#         bot = CLI()
#         bot.main()
#     except Exception as e:
#         print(f"Error faltal {e}")