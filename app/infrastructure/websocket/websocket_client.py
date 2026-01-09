import websocket
from websocket import WebSocketApp
import threading
import time
import random
import json
import logging
from typing import Any, Optional, Union

logging.basicConfig(
    level=logging.INFO
)

logger = logging.getLogger(__name__)

class WebSocketClient:
    def __init__(
        self,
        url: str,
        headers: dict[str, Any] | None = None,
        heartbeat_interval: int = 30,
        reconnect: bool = True,
        max_reconnect_delay: int = 60,
    ):
        self.url = url
        self.headers = headers or {}
        self.heartbeat_interval = heartbeat_interval
        self.reconnect = reconnect
        self.max_reconnect_delay = max_reconnect_delay

        self.ws: websocket.WebSocketApp | None = None
        self._thread: threading.Thread | None = None
        self._stop_event = threading.Event()
        self._reconnect_attempts = 0


    def _on_open(self, ws: WebSocketApp):
        logger.info("WebSocket conectado")
        self._reconnect_attempts = 0

    def _on_message(self, ws: WebSocketApp, message: Union[str, bytes]):
        logger.info(f"Mensaje recibido: {message}")

    def _on_error(self, ws: WebSocketApp, error: Exception):
        logger.error(f"Error WebSocket: {error}")

    def _on_close(self, ws: WebSocketApp, close_status_code: Optional[int], close_msg: Optional[str]):
        logger.warning(
            f"WebSocket cerrado: code={close_status_code}, msg={close_msg}"
        )


    def _run(self):
        while not self._stop_event.is_set():
            self.ws = websocket.WebSocketApp(
                self.url,
                header=[f"{k}: {v}" for k, v in self.headers.items()],
                on_open=self._on_open,
                on_message=self._on_message,
                on_error=self._on_error,
                on_close=self._on_close,
            )

            try:
                self.ws.run_forever( # type: ignore
                    ping_interval=self.heartbeat_interval,
                    ping_timeout=10,
                )
            except Exception as e:
                logger.exception(f"Excepción en run_forever: {e}")

            if not self.reconnect or self._stop_event.is_set():
                break

            delay = self._calculate_backoff()
            logger.info(f"Reconectando en {delay:.1f}s...")
            time.sleep(delay)

    def _calculate_backoff(self) -> float:
        self._reconnect_attempts += 1
        base = min(
            self.max_reconnect_delay,
            2 ** self._reconnect_attempts
        )
        jitter = random.uniform(0, 1)
        return base + jitter

    def start(self):
        if self._thread and self._thread.is_alive():
            return

        self._stop_event.clear()
        self._thread = threading.Thread(
            target=self._run,
            daemon=True
        )
        self._thread.start()

    def stop(self):
        self._stop_event.set()
        if self.ws:
            try:
                self.ws.close() # type: ignore
            except Exception:
                pass
        if self._thread:
            self._thread.join(timeout=5)

    def send_json(self, data: dict[str, Any] | str):
        if not self.ws:
            raise RuntimeError("WebSocket no conectado")

        payload = data if isinstance(data, str) else json.dumps(data)
        self.ws.send(payload)

    def send(self, message: str | str):
        if not self.ws:
            raise RuntimeError("WebSocket no conectado")

        self.ws.send(message)
