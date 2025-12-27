import os
import sys
import threading
import webbrowser
import uvicorn
import time
from pathlib import Path
from dotenv import load_dotenv
from main import app  # type: ignore

def get_project_root() -> Path:
    """raiz del proyecto."""
    if getattr(sys, 'frozen', False):
        # crear una ruta para la cache de tiktoken dentro de la carpeta temporal del exe
        meipass = getattr(sys, '_MEIPASS', os.getcwd())
        os.environ["TIKTOKEN_CACHE_DIR"] = os.path.join(meipass, "tiktoken_cache")
        return Path(sys.executable).parent
    return Path(__file__).resolve().parent

def open_browser(url: str):
    """espera un momento y abrir el navegador"""
    time.sleep(7.0)
    webbrowser.open(url)

def run_app():
    root = get_project_root()
    load_dotenv(root / ".env")
    
    host = os.getenv("HOST_SERVER", "127.0.0.1")
    port = int(os.getenv("PORT_SERVER", 8000))
    url = f"http://{host}:{port}"
    
    if not os.environ.get("UVICORN_CORE_LOOP"):
        threading.Thread(target=open_browser, args=(url,), daemon=True).start()

    try:
        uvicorn.run(
            "main:app", 
            host=host, 
            port=port, 
            reload=False, 
            workers=1,
            use_colors=False,
            log_config=None
        )
    except Exception as e:
        print(f"\nFATAL ERROR: {e}")
        input("\nPresiona Enter para salir...")

if __name__ == "__main__":
    run_app()