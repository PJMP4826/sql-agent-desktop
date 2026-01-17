class FormatDataLLMPrompts:
    GENERATE_EXCEL = """
    Genera datos para un reporte Excel basado en esta solicitud:
    {query}

    Utilizando los siguientes datos:
    {data}
    
    IMPORTANTE: Retorna SOLO el JSON con esta estructura exacta.
    Asegúrate de que todas las filas tengan el mismo número de columnas que los headers.
    """

    @classmethod
    def format_with_context(cls, query: str, data: str) -> str:
        return cls.GENERATE_EXCEL.format(query=query, data=data)
