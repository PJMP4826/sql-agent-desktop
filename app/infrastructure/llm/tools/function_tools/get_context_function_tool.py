from app.infrastructure.llm.tools.get_context_conversation import GetContextConversation

from llama_index.core.tools import FunctionTool


def create_get_context_function_tool(
    get_context_tool: GetContextConversation,
) -> FunctionTool:
    """
    Crear una FunctionTool para que el agente pueda obtener contexto del
    RAG para aclarar peticiones abiguas del usuario

    Args:
        get_context_tool: instancia de GetContextConversation configurada

    Returns:
        FunctionTool listo para usar en el agente
    """

    def get_context(agent_question: str) -> str:
        response = get_context_tool.get_context(agent_question=agent_question)
        print("Context de conversacion: ", response)

        return response

    tool = FunctionTool.from_defaults(
        fn=get_context,
        name="get_context_conversation",
        description=(
            "Herramienta para recuperar información contextual relevante desde un sistema RAG. "
            "Usala cuando la consulta del usuario sea ambigua o poco clara, y necesites contexto adicional en lenguaje natural para clarificar y comprender mejor su intención antes de generar una confirmacion"
            "Entrada: una pregunta formulada por el agente (LLM), expresando cualquier duda o necesidad de aclaración sobre la petición original del usuario"
            "Salida: información contextual adicional que ayuda a entender con mayor precisión lo que el usuario está solicitando."
        ),
    )

    return tool
