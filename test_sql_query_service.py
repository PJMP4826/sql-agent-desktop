from app.infrastructure.services.sql_query_service import SQLQueryService
from app.infrastructure.llm.gemini.client import GeminiAdapter
from app.config.settings import Settings
from app.infrastructure.database.sql.connection_manager import ConnetionManager
from app.infrastructure.database.sql.sql_database_adapter import SQLDatabaseAdapter

settings = Settings() # type: ignore

gemini_client = GeminiAdapter(
    llm_model_name=settings.llm_gemini_model,
    api_key=settings.google_api_key,
    embed_model=settings.embed_model_name
)

connection_manager = ConnetionManager(settings)
sql_adapter = SQLDatabaseAdapter(connection_manager=connection_manager)

TABLES = [
    "admClientes"
]

business_context = """
Esta es una tabla unificada que almacena tanto clientes como proveedores. El identificador único es CIDCLIENTEPROVEEDOR. Cada registro tiene un código en CCODIGOCLIENTE de 30 caracteres y la razón social en CRAZONSOCIAL de 60 caracteres.
"""

sql_query_service = SQLQueryService(
    llm_client=gemini_client,
    connection_manager=connection_manager,
    sql_adapter=sql_adapter,
    include_tables=TABLES,
    business_context=business_context,
    verbose_sql=True
) 

def main():
    try:
        while True:
            user_input = input("Tu: ").strip()
            
            if user_input.lower() in ["salir", "exit", "quit"]:
                print("Adios!")
                break
            
            if not user_input:
                continue
            
            try:
                response = sql_query_service.query(user_input)
                print(f"\nAgent: {response}\n")
            except Exception as e:
                print(f"\nError: {e}\n")
    
    except KeyboardInterrupt:
        print("\n\nInterrupted. Goodbye!")
    except Exception as e:
        print(f"Fatal error: {e}")


if __name__ == "__main__":
    main()