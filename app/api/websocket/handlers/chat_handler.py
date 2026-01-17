from fastapi import WebSocket, WebSocketDisconnect
from app.api.websocket.connection_manager import ConnectionManager
from app.application.agents.sql_agent.sql_agent import SQLAgent
from app.infrastructure.services.token_counter import TokenCounter
from app.application.services.excel_result_extractor import ExcelResultExtractor


async def handle_request(websocket: WebSocket) -> str:
    data = await websocket.receive_text()
    user_message = data.strip()
    return user_message


async def validate_user_input(
    usert_input: str, manager: ConnectionManager, websocket: WebSocket
) -> bool:
    if not usert_input:
        await manager.send_message(
            "AI: Porfavor escribe un mensaje antes de enviar.", websocket
        )
        return False

    if usert_input.lower() == "exit":
        await manager.send_message("AI: Terminando sesion.", websocket)
        manager.disconnect(websocket)
        raise WebSocketDisconnect(code=100)

    return True


async def handle_agent_response(
    user_input: str,
    manager: ConnectionManager,
    websocket: WebSocket,
    sql_agent: SQLAgent,
    token_counter: TokenCounter,
):
    try:

        # await manager.send_message("Escribiendo...", websocket)

        response = await sql_agent.chat(user_input=user_input)

        extractor = ExcelResultExtractor()

        if extractor.has_excel(response=response):
            excel_file = extractor.get_excel_file(response=response)
            await manager.send_message_json(
                message=excel_file.to_websocket_message(),
                websocket=websocket,
            )

        response_txt = response.response_text

        print("Response de agent: ", response_txt)

        print(f"\nTotal LLM Prompt Tokens: {token_counter.prompt_llm_token_count()}")
        print(
            f"Total LLM Completion Tokens: {token_counter.completion_llm_token_count()}"
        )
        print(f"Total LLM Tokens: {token_counter.total_llm_token_count()}")
        print(f"Total Embedding Tokens: {token_counter.total_embedding_token_count()}")

        await manager.send_message_json(
            message={"type": "message", "content": str(response_txt)},
            websocket=websocket,
        )  # type: ignore

    except Exception as e:
        print("Error en la query: ", e)
        await manager.send_message_json(
            message={
                "type": "error",
                "content": str(e),
            },
            websocket=websocket,
        )
