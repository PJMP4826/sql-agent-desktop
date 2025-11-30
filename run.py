import os
import threading
import webbrowser
import uvicorn
from main import app
from dotenv import load_dotenv

load_dotenv()

HOST: str = str(os.getenv("HOST_SERVER"))
PORT: int = int(os.getenv("PORT_SERVER"))
URL: str = f"http://{HOST}:{PORT}"

def open_browser():
    webbrowser.open(URL)

if __name__ == "__main__":
    threading.Timer(5.0, open_browser).start()
    
    
    uvicorn.run(
        "main:app", 
        host=HOST, 
        port=PORT,
        reload=True,
        workers=1 
    )