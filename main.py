from fastapi import FastAPI, WebSocket, WebSocketDisconnect, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from src.api.presentation.websocket.connection_manager import ConnectionManager
from src.api.presentation.websocket.chat_handler import handle_request, validate_user_input, handle_rag_response
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

app = FastAPI(
    title="AI Chat API",
    docs_url="/docs",
    description="This API allows you to chat with an AI model using WebSocket connections.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter(prefix="/chat", tags=["Chat"])
manager = ConnectionManager()


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    try:
        await manager.connect(websocket)

        while True:
            user_input = await handle_request(websocket)
            print("User: ", user_input)

            puede_procesar = await validate_user_input(user_input, manager, websocket)

            if not puede_procesar:
                continue

            await handle_rag_response(user_input, manager, websocket)

    except WebSocketDisconnect as e:
        print("Cliente desconectado")
        manager.disconnect(websocket)
    finally:
        await websocket.close()

app.include_router(router)
