from fastapi import WebSocket, WebSocketDisconnect, APIRouter
from app.api.websocket.connection_manager import ConnectionManager
from app.api.websocket.handlers.chat_handler import handle_request, validate_user_input, handle_agent_response
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/chat", tags=["Chat"])
manager = ConnectionManager()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    client_id = id(websocket)
    logger.info(f"Nuevo WebSocket conexion client_id: {client_id}")

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
        logger.info(f"Client {client_id} desconectado: code={e.code}")
        manager.disconnect(websocket)
    
    except Exception as e:
        logger.exception(f"Error WebSocket para client {client_id}: {e}")
        manager.disconnect(websocket)
        
        try:
            await websocket.close(code=1011, reason="Internal server error")
        except:
            pass
    
    finally:
        manager.disconnect(websocket)
        logger.info(f"Client {client_id} clean")