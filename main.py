import os
import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from src.api.websocket import ConnectionManager
from src.core.rag import RAG
import warnings

warnings.filterwarnings("ignore", category=UserWarning)
load_dotenv()

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
    api_key = os.getenv("GOOGLE_API_KEY")

    # if not api_key:
    #     print("No hay api key")
    #     await manager.send_message("AI: Error - No se encontro la API key", websocket)
    #     await websocket.close()
    #     return

    try:
        await manager.connect(websocket)
        rag_instance = RAG(api_key=api_key)

        while True:
            data = await websocket.receive_text()
            print("Texto recibido: ", data)

            user_message = data.strip()

            if not user_message:
                await manager.send_message("AI: Porfavor escribe un mensaje antes de enviar.", websocket)
                continue

            if user_message.lower() == "exit":
                await manager.send_message("AI: Terminando sesion.", websocket)
                manager.disconnect(websocket)
                break

            try:
                response = await asyncio.to_thread(
                    rag_instance.procesar_query, user_message
                )
            except Exception as e:
                print("Error en la query: ", e)
                await manager.send_message(f"AI: Error interno - {e}", websocket)
                continue

            await manager.send_message(f"AI: {response}", websocket)

    except WebSocketDisconnect as e:
        print("Cliente desconectado")
        manager.disconnect(websocket)
    finally:
        await websocket.close()


app.include_router(router)
