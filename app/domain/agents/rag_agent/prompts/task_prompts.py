from typing import List


class TaskPrompts:
    BASIC_TABLE_CONTEXT = """
    Pregunta del usuario: {user_query}

    Tablas relevantes: {tables_list}

    Basándote en la documentación del schema de CONTPAQi Comercial, proporciona:

    1. Qué representa cada tabla en el contexto del sistema
    2. Qué campos específicos de cada tabla son relevantes para esta consulta
    3. Consideraciones importantes sobre estas tablas

    Responde de forma clara y concisa (sin saturar), enfocándose en información útil para generar SQL.
    """

    COMBINE_CONTEXT_CONTEXT_BUILDER = """
    CONTEXTO PARA GENERACIÓN DE SQL

    Tablas seleccionadas: {tables_selected}

    INFORMACIÓN DE LAS TABLAS:
    {basic_context}

    RELACIONES LÓGICAS ENTRE TABLAS:
    {relationships}

    IMPORTANTE:
    - Estas son relaciones lógicas (no físicas) mediante campos de ID
    - Usa JOINs apropiados según las relaciones mostradas
    - Verifica que los campos existan en las tablas antes de usarlos
    """

    @classmethod
    def format_basic_table_context(
        cls, user_query: str, tables_relavantes: List[str]
    ) -> str:
        return cls.BASIC_TABLE_CONTEXT.format(
            user_query=user_query, tables_list=tables_relavantes
        )

    @classmethod
    def format_combine_context(
        cls, tables_selected: List[str], basic_context: str, relationships: str
    ) -> str:
        return cls.COMBINE_CONTEXT_CONTEXT_BUILDER.format(
            tables_selected=tables_selected,
            basic_context=basic_context,
            relationships=relationships,
        )
