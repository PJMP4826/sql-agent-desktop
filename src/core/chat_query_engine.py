import os
from pathlib import Path
from dotenv import load_dotenv
from typing import List, Optional, Dict

load_dotenv()


class ChatQueryEngine:
    def __init__(self):
        self.system_prompt_rol = ""
        self.cargarRolBot()

    def cargarRolBot(self):
        directorio_actual = Path(os.path.dirname(os.path.abspath(__file__)))

        ruta_absoluta_txt = directorio_actual.parent / "config" / "rol_bot_sql.txt"

        with open(ruta_absoluta_txt, "r", encoding="utf-8") as f:
            rol_bot = f.read()

        self.system_prompt_rol = rol_bot

if __name__ == "__main__":
    chat_engine = ChatQueryEngine()
    print(chat_engine.system_prompt_rol)

