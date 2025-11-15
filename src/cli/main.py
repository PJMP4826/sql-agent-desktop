import os
from dotenv import load_dotenv
from src.core.rag import RAG

class CLI:
    def main(self):
        load_dotenv()
        api_key = os.getenv("GOOGLE_API_KEY")

        if not api_key:
            print("Error: No se encontro la api key")
            return

        try:
            rag_instance = RAG()
            
            while True:
                user_input = input("Tú: ")
                if user_input.lower() in ["salir", "exit"]:
                    print("Adios")
                    break
                
                response = rag_instance.procesar_query(user_input)
                print(f"Bot: {response}")

        except (ValueError, RuntimeError) as e:
            print(f"Error fatal durante la iniciapizacion del bot: {e}")

if __name__ == "__main__":

    try:
        bot = CLI()
        bot.main()
    except Exception as e:
        print(f"Error faltal {e}")