from llama_index.core.prompts import PromptTemplate


class SQLPrompts:

    TEXT_TO_SQL_BASE = """
        Schema: {schema}

        Rules (SQL Server):
        1. Use ONLY schema columns/tables (no inventions)
        2. No assumed relationships (exact column matches only)
        3. Simple queries preferred
        4. No comments or explanations
        5. TOP 20 limit
        6. SQL Server syntax only

        Question: {query_str}

        SQLQuery:
        """

    TEXT_TO_SQL_WITH_CONTEXT = """
            Schema: {schema}

            Context: {business_context}

            Question: {query_str}

            RULES:
            1. Use JOINs when business context shows relationships (prefer INNER JOIN)
            2. Subqueries only if necessary with matching ID columns
            3. SQL Server syntax only
            4. TOP 20 or user-specified limit
            5. Use UPPER() and LIKE '%' input '%' for text matching (data is uppercase) when necessary
            6. If ambiguous, choose simplest interpretation

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
            "business_context", business_context
        )
