import json
from src.config.tables_conocidas import tables_conocidas
from src.core.rag import RAG


class SchemaLoader:

    def __init__(self):
        self.rag_instance = RAG()
        self.known_tables_set = set(tables_conocidas)

    def inferir_tables_from_query(self, user_query: str):
        try:
            if not user_query or not user_query.strip():
                print("Error: La consulta está vacía")
                return []

            response = self.rag_instance.procesar_query(user_input=user_query)
            print("Tabla inferida por el RAG: ", response)

            response_clean = response.strip()

            import re

            json_match = re.search(r"\[.*?\]", response_clean, re.DOTALL)
            if json_match:
                response_clean = json_match.group(0)

            tables_selected_list = json.loads(response_clean)

            if not isinstance(tables_selected_list, list):
                print(f"Error: La respuesta no es una lista: {tables_selected_list}")
                return []

            # filtrar valores no string
            tables_selected_list = [
                t for t in tables_selected_list if isinstance(t, str)
            ]

            selected_tables_set = set(tables_selected_list)
            tables_to_use = selected_tables_set.intersection(self.known_tables_set)
            tables_selected = list(tables_to_use)

            if not tables_selected:
                print(
                    "Advertencia: Ninguna de las tablas inferidas es valida o conocida."
                )
                print(f"Tablas inferidas: {tables_selected_list}")
                print(
                    f"Tablas conocidas disponibles: {list(self.known_tables_set)[:10]}..."
                )

            print(f"Tablas filtradas y listas para usar: {tables_selected}")
            return tables_selected

        except json.JSONDecodeError as e:
            print(f"Error: La respuesta del modelo no es un JSON valido: {e}")
            print(f"Respuesta recibida: {response[:500]}")
            return []
        except Exception as e:
            print(f"Error general en la query: {e}")
            import traceback

            traceback.print_exc()
            return []

    def obtener_contexto_negocio(self, user_query: str, tables_selected: list[str]):
        try:
            # informacion basica de las tablas
            prompt_completo = f"""
            Pregunta del usuario: {user_query}

            Tablas relevantes para responder: {', '.join(tables_selected)}

            Basándote en la documentación del esquema de CONTPAQi Comercial, proporciona:
            1. Qué representan estas tablas en el contexto del sistema
            2. Qué campos específicos de cada tabla usarías para responder la pregunta del usuario
            3. Cómo se relacionan estas tablas entre sí según la documentación, incluyendo los nombres exactos de los campos que las relacionan

            Responde de forma clara y concisa, enfocándote en la información relevante para generar la consulta SQL.
            """

            response = self.rag_instance.query_engine.query(prompt_completo)
            contexto_basico = str(response).strip()

            relaciones_logicas = self._obtener_relaciones_logicas(tables_selected)

            contexto_completo = f"""
                {contexto_basico}

                RELACIONES LÓGICAS ENTRE LAS TABLAS SELECCIONADAS:
                {relaciones_logicas}

                IMPORTANTE: Estas son relaciones lógicas (no físicas) mediante campos de ID. Úsalas con JOINs cuando sea necesario.
            """

            return contexto_completo.strip()

        except Exception as e:
            print(f"Error al generar el contexto de negocio: {e}")
            return ""

    def _obtener_relaciones_logicas(self, tables: list[str]) -> str:
        relaciones_mapeo = {
            "admDocumentos": {
                "admClientes": "admDocumentos.CIDCLIENTEPROVEEDOR = admClientes.CIDCLIENTEPROVEEDOR",
                "admConceptos": "admDocumentos.CIDCONCEPTODOCUMENTO = admConceptos.CIDCONCEPTODOCUMENTO",
                "admAgentes": "admDocumentos.CIDAGENTE = admAgentes.CIDAGENTE",
                "admMonedas": "admDocumentos.CIDMONEDA = admMonedas.CIDMONEDA",
                "admMovimientos": "admDocumentos.CIDDOCUMENTO = admMovimientos.CIDDOCUMENTO",
            },
            "admMovimientos": {
                "admProductos": "admMovimientos.CIDPRODUCTO = admProductos.CIDPRODUCTO",
                "admAlmacenes": "admMovimientos.CIDALMACEN = admAlmacenes.CIDALMACEN",
                "admDocumentos": "admMovimientos.CIDDOCUMENTO = admDocumentos.CIDDOCUMENTO",
            },
            "admClientes": {
                "admAgentes": "admClientes.CIDAGENTEVENTA = admAgentes.CIDAGENTE OR admClientes.CIDAGENTECOBRO = admAgentes.CIDAGENTE",
                "admMonedas": "admClientes.CIDMONEDA = admMonedas.CIDMONEDA",
                "admAlmacenes": "admClientes.CIDALMACEN = admAlmacenes.CIDALMACEN",
            },
            "admProductos": {
                "admMonedas": "admProductos.CIDMONEDA = admMonedas.CIDMONEDA",
            },
        }

        relaciones_texto = []
        for i, tabla1 in enumerate(tables):
            if tabla1 in relaciones_mapeo:
                for tabla2 in tables[i + 1 :]:
                    if tabla2 in relaciones_mapeo[tabla1]:
                        relaciones_texto.append(
                            f"- {tabla1} ↔ {tabla2}: {relaciones_mapeo[tabla1][tabla2]}"
                        )
                    # relacion inversa
                    elif (
                        tabla2 in relaciones_mapeo
                        and tabla1 in relaciones_mapeo[tabla2]
                    ):
                        relaciones_texto.append(
                            f"- {tabla2} ↔ {tabla1}: {relaciones_mapeo[tabla2][tabla1]}"
                        )

        if not relaciones_texto:
            return "No se encontraron relaciones logicas directas documentadas entre estas tablas. Considera usar subconsultas o consultas separadas."

        return "\n".join(relaciones_texto)
