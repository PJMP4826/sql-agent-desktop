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
