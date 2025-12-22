import os
import threading
import webbrowser
import uvicorn
from main import app  # type: ignore
from dotenv import load_dotenv

load_dotenv()

HOST: str = str(os.getenv("HOST_SERVER"))
PORT: int = int(os.getenv("PORT_SERVER"))  # type: ignore
URL: str = f"http://{HOST}:{PORT}"
INTERVAL = 6.0


def open_browser():
    webbrowser.open(URL)


def open_browser_interval():
    threading.Timer(INTERVAL, open_browser).start()


def run_server():
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True, workers=1)


if __name__ == "__main__":
    try:
        open_browser_interval()
        run_server()
    except Exception as e:
        print("Error: ", e)
