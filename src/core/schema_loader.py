import json
from src.config.tables_conocidas import tables_conocidas
from src.core.rag import RAG


class SchemaLoader:

    def __init__(self):
        self.rag_instance = RAG()
        self.known_tables_set = set(tables_conocidas)

    def inferir_tables_from_query(self, user_query: str):
        try:
            response = self.rag_instance.procesar_query(user_input=user_query)
            print("Tabla inferida por el RAG: ", response)

            tables_selected_list = json.loads(response)

            selected_tables_set = set(tables_selected_list)

            tables_to_use = selected_tables_set.intersection(self.known_tables_set)

            tables_selected = list(tables_to_use)

            if not tables_selected:
                print(
                    "Advertencia: Ninguna de las tablas inferidas es valida o conocida."
                )

            print(f"Tablas filtradas y listas para usar: {tables_selected}")
            return tables_selected

        except json.JSONDecodeError as e:
            print(f"Error: La respuesta del modelo no es un JSON valido: {e}")
            return []
        except Exception as e:
            print(f"Error general en la query: {e}")
            return []
        
    def obtener_contexto_negocio(self, user_query: str, tables_selected: list[str]):
        try:
            prompt_completo = f"""
            Pregunta del usuario: {user_query}

            Tablas relevantes para responder: {', '.join(tables_selected)}

            Basándote en la documentación del esquema de CONTPAQi Comercial, explica en español:
            1. Qué representan estas tablas en el contexto del sistema
            2. Qué campos específicos de cada tabla usarías para responder la pregunta del usuario
            3. Cómo se relacionan estas tablas entre sí según la documentación

            Responde de forma clara y concisa, enfocándote en la información relevante para generar la consulta SQL.
            """

            response = self.rag_instance.query_engine.query(prompt_completo)
            return str(response).strip()
        
        except Exception as e:
            print(f"Error al generar el contexto de negocio: {e}")
            return ""
