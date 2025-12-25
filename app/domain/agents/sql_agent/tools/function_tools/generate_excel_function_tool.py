from app.domain.agents.sql_agent.tools.generate_excel_tool import generate_excel_report
from llama_index.core.tools import FunctionTool


def create_generate_excel_function_tool() -> FunctionTool:
    tool = FunctionTool.from_defaults(
        fn=generate_excel_report,
        name="generate_excel_report",
        description=(
            """
            Herramienta para generar un archivo excel
            Entrada: String JSON con la estructura:
              {"sheets": [{"name": "Sheet1", "headers": [...], "rows": [[...]]}]}"
                filename: Nombre del archivo Excel a generar
            Salida: Dict python con el archivo en base64 y metadata
            Usa esta herramienta cuando el usuario pida generar reportes en excel
            """
        ),
    )

    return tool
