from app.domain.agents.sql_agent.tools.generate_excel_tool import generate_excel_report
from llama_index.core.tools import FunctionTool
from app.application.ports.llm_port import LLMPort
from app.domain.agents.sql_agent.prompts.format_data_llm_prompts import (
    FormatDataLLMPrompts,
)
from typing import Any
from app.domain.schemas.excel_report_schema import ExcelReport


def create_generate_excel_function_tool(llm_client: LLMPort) -> FunctionTool:
    def get_excel_data_from_gemini(query: str, data: str) -> str:
        """
        Usa Gemini con schema controlado para generar datos de Excel
        """
        try:
            print("Query para gemini: ", query)
            print("Data para Gemini: ", data)

            prompt = FormatDataLLMPrompts.format_with_context(query=query, data=data)

            response = llm_client.generate_content(prompt=prompt)

            # Gemini retorna JSON valido
            return response
        except Exception as e:
            print(f"Error generando datos JSON con Gemini: {str(e)}")
            return f"Error generando datos JSON con Gemini: {str(e)}"

    def generate_excel_with_gemini(
        query: str, data: str, filename: str = "reporte.xlsx"
    ) -> dict[str, Any]:
        try:
            # Obtener datos estructurados de Gemini
            json_data = get_excel_data_from_gemini(query, data)

            print("JSON Data Generate Gemini: ", json_data)

            ExcelReport.model_validate_json(json_data)

            return generate_excel_report(json_data, filename)

        except Exception as e:
            return {
                "type": "error",
                "success": False,
                "message": f"Error generando Excel con Gemini: {str(e)}",
            }

    tool = FunctionTool.from_defaults(
        fn=generate_excel_with_gemini,
        name="generate_excel_report",
        description=(
            """
            Genera un reporte Excel con datos reales.
            
            Parametros REQUERIDOS:
            - query: Descripcion del formato del reporte (ej: "columnas ID, Nombre, Email")
            - data: STRING JSON con los datos reales obtenidos de la consulta SQL
            - filename: Nombre del archivo (default: reporte.xlsx)
            
            IMPORTANTE: Siempre debes pasar los datos reales de la última consulta SQL.
            
            Ejemplo de uso:
            1. Primero obtienes los datos de la base de datos
            2. Luego llamas a esta tool pasando:
               - query: "Reporte de clientes con columnas ID, Nombre, RFC"
               - data: '[{"id": 1, "nombre": "Juan", "rfc": "ABC123"}, ...]'
               - filename: "nombre_excel.xlsx"
            
            NO inventes datos. Usa siempre los datos del resultado de la consulta SQL previa.
            """
        ),
    )

    return tool
