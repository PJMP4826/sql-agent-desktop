# app/domain/agents/sql_agent/prompts/sql_prompts.py

from llama_index.core.prompts import PromptTemplate


class SQLPrompts:

    TEXT_TO_SQL_BASE = """
        Esquema de base de datos:
        {schema}

        REGLAS:
        1. Usa SOLO columnas y tablas del esquema (no inventes nada)
        2. NO asumas relaciones - usa solo columnas que coincidan exactamente
        3. Prefiere consultas simples
        4. NO agregues comentarios ni texto explicativo
        5. Usa TOP 20 para limitar resultados
        6. Sintaxis SQL Server únicamente

        Pregunta: {query_str}

        SQLQuery:
        """

    TEXT_TO_SQL_WITH_CONTEXT = """
            Esquema: {schema}

            Contexto explicativo: {business_context}

            Pregunta: {query_str}

            Genera SQL valido para SQL Server. Solo el query, sin explicaciones.
            Usa subconsultas solo si es necesario y SOLO si existe una columna coincidente entre tablas.
            Usa TOP 20 o el limite que especifique el usuario. No inventes columnas.

            SQLQuery:
            """

    @classmethod
    def get_text_to_sql_prompt(
        cls, include_business_context: bool = False
    ) -> PromptTemplate:
        if include_business_context:
            return PromptTemplate(cls.TEXT_TO_SQL_WITH_CONTEXT)
        else:
            return PromptTemplate(cls.TEXT_TO_SQL_BASE)

    @classmethod
    def format_with_context(cls, business_context: str) -> str:
        return cls.TEXT_TO_SQL_WITH_CONTEXT.replace(
            "business_context",
            business_context
        )
