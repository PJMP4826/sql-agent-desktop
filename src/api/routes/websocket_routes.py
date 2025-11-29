from fastapi import WebSocket, WebSocketDisconnect, APIRouter
from src.api.presentation.websocket.connection_manager import ConnectionManager
from src.api.presentation.websocket.chat_handler import handle_request, validate_user_input, handle_agent_response

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

            await handle_agent_response(user_input, manager, websocket)

    except WebSocketDisconnect as e:
        print("Cliente desconectado")
        manager.disconnect(websocket)
    finally:
        await websocket.close()