import os
import asyncio
from src.core.rag import RAG
from src.api.presentation.websocket.agent_handler import AgentHandler
from dotenv import load_dotenv
from fastapi import WebSocket, WebSocketDisconnect
from src.api.presentation.websocket.connection_manager import ConnectionManager

# rag_instance = RAG()
agent_instance = AgentHandler()

async def handle_request(websocket: WebSocket) -> str:
    data = await websocket.receive_text()
    user_message = data.strip()
    return user_message


async def validate_user_input(usert_input: str, manager: ConnectionManager, websocket: WebSocket) -> bool:
    if not usert_input:
        await manager.send_message("AI: Porfavor escribe un mensaje antes de enviar.", websocket)
        return False

    if usert_input.lower() == "exit":
        await manager.send_message("AI: Terminando sesion.", websocket)
        manager.disconnect(websocket)
        raise WebSocketDisconnect(code=100)
    
    return True


# async def handle_rag_response(user_input: str, manager: ConnectionManager, websocket: WebSocket):
#     try:
#         response = await asyncio.to_thread(
#             rag_instance.procesar_query, user_input
#         )
#     except Exception as e:
#         print("Error en la query: ", e)
#         await manager.send_message(f"AI: Error interno - {e}", websocket)

#     await manager.send_message(f"AI: {response}", websocket)

async def handle_agent_response(user_input: str, manager: ConnectionManager, websocket: WebSocket):
    try:
        response = await agent_instance.chat(user_input)
        
    except Exception as e:
        print("Error en la query: ", e)
        await manager.send_message(f"AI: Error interno - {e}", websocket)

    await manager.send_message(f"{response}", websocket)