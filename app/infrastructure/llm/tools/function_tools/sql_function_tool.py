from llama_index.core.tools import FunctionTool
from app.infrastructure.llm.tools.sql_query_tool import SQLQueryTool


def create_sql_query_function_tool(sql_query_tool: SQLQueryTool) -> FunctionTool:
    """
    Crear FunctionTool para que el agente pueda ejecutar queries SQL.

    Args:
        sql_query_tool: Instancia de SQLQueryTool configurada

    Returns:
        FunctionTool listo para usar en el agente
    """

    def execute_sql_query(user_question: str) -> str:
        """
        Ejecuta una consulta SQL a partir de una pregunta en lenguaje natural.

        Esta herramienta convierte la pregunta de un usuario en lenguaje natural a una consulta SQL,
        la ejecuta en la base de datos y devuelve los resultados.

        Args:
            user_question: La pregunta del usuario en lenguaje natural.

        Returns:
            Los resultados de la consulta como una cadena de texto (string) formateada.
        """
        result = sql_query_tool.execute_nl_query(user_question, verbose=False)

        return result

    # Crear FunctionTool
    tool = FunctionTool.from_defaults(
        fn=execute_sql_query,
        name="sql_query",
        description=(
            "Consulta la base de datos de CONTPAQi® Comercial usando lenguaje natural"
            "Traduce automáticamente la pregunta a SQL y ejecuta la consulta.\n\n"
            "Úsala para preguntas sobre:\n"
            "- Ventas, facturación, ingresos\n"
            "- Clientes, proveedores, agentes\n"
            "- Inventarios, productos, almacenes\n"
            "- Documentos, pagos, saldos\n"
            "- Análisis, reportes, estadísticas\n\n"
            "Entrada: Pregunta completa en lenguaje natural\n"
            "Salida: Datos estructurados/lenguaje natural con la respuesta"
        ),
    )

    return tool
