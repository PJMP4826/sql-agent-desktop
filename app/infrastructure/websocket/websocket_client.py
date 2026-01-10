import websocket
from websocket import WebSocketApp
import threading
import time
import random
import json
import logging
from typing import Any, Optional, Union
from queue import Queue, Empty
from app.shared.infrastructure_exceptions import InfrastructureException

logging.basicConfig(level=logging.INFO)

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
        self.incoming = Queue() # type: ignore
        self._connected_event = threading.Event()
        self._last_error: Optional[Exception] = None

    def _on_open(self, ws: WebSocketApp):
        self.ws = ws
        self._reconnect_attempts = 0  # resetear intentos de reconexion
        self._last_error = None
        self._connected_event.set()
        logger.info(f"WebSocket conectado a {self.url}")

    def _on_message(self, ws: WebSocketApp, message: Union[str, bytes]):
        """Callback cuando se recibe un mensaje"""
        logger.debug(f"Mensaje recibido ({len(str(message))} bytes)")
        self.incoming.put(message) # type: ignore

    def _on_error(self, ws: WebSocketApp, error: Exception):
        """Callback cuando ocurre un error"""
        self._last_error = error
        logger.error(f"Error WebSocket: {error}")

    def _on_close(self, ws: WebSocketApp, close_status_code: Optional[int], close_msg: Optional[str]):
        """Callback cuando el WebSocket se cierra"""
        logger.warning(f"WebSocket cerrado: code={close_status_code}, msg={close_msg}")
        self._connected_event.clear()

    def _run(self):        
        while not self._stop_event.is_set():
            try:
                logger.debug(f"Conectando a {self.url}...")
                
                self.ws = websocket.WebSocketApp(
                    self.url,
                    header=[f"{k}: {v}" for k, v in self.headers.items()],
                    on_open=self._on_open,
                    on_message=self._on_message,
                    on_error=self._on_error,
                    on_close=self._on_close,
                )

                self.ws.run_forever( # type: ignore
                    ping_interval=self.heartbeat_interval,
                    ping_timeout=10,
                )
                
            except Exception as e:
                self._last_error = e
                logger.exception(f"Excepcion en run_forever: {e}")

            if not self.reconnect or self._stop_event.is_set():
                break

            delay = self._calculate_backoff()
            time.sleep(delay)

    def _calculate_backoff(self) -> float:
        self._reconnect_attempts += 1
        base = min(self.max_reconnect_delay, 2 ** self._reconnect_attempts)
        jitter = random.uniform(0, 1)
        return base + jitter

    def start(self):
        """Inicia el cliente WebSocket en un thread separado"""
        if self._thread and self._thread.is_alive():
            return

        self._stop_event.clear()
        self._thread = threading.Thread(
            target=self._run,
            daemon=True,
            name="WebSocketClientThread"
        )
        self._thread.start()
        logger.info("Cliente WebSocket iniciado")

    def stop(self):
        logger.info("deteniendo cliente WebSocket")
        self._stop_event.set()
        
        if self.ws:
            try:
                self.ws.close() # type: ignore
            except Exception as e:
                logger.error(f"Error al cerrar WebSocket: {e}")
        
        if self._thread:
            self._thread.join(timeout=5)
            
        logger.info("Cliente WebSocket detenido")

    def is_connected(self) -> bool:
        return self._connected_event.is_set() and self.ws is not None

    def wait_for_connection(self, timeout: float = 10.0) -> bool:
        connected = self._connected_event.wait(timeout)
        
        if not connected and self._last_error:
            logger.error(f"Timeout. Ultimo error: {self._last_error}")
            
        return connected

    def send(self, message: str, timeout: float = 5.0):
        # esperar la conexion
        if not self._connected_event.wait(timeout):
            error_msg = f"WebSocket no conectado despues de {timeout}s"
            if self._last_error:
                error_msg += f". Ultimo error: {self._last_error}"
            raise InfrastructureException(error_msg)

        if not self.ws:
            raise InfrastructureException("WebSocket no disponible")
        
        try:
            logger.debug(f"Enviando mensaje ({len(message)} bytes)")
            self.ws.send(message)
            logger.debug("Mensaje enviado")
        except Exception as e:
            logger.error(f"Error al enviar mensaje: {e}")
            raise InfrastructureException(f"Error al enviar mensaje: {str(e)}")

    def send_json(self, data: dict[str, Any]):
        payload = json.dumps(data)
        self.send(payload)

    def receive(self, timeout: float | None = None) -> Union[str, bytes, None]:
        try:
            message = self.incoming.get(timeout=timeout) # type: ignore
            return message # type: ignore
        except Empty:
            logger.debug("Timeout esperando mensaje")
            return None

    def receive_json(self, timeout: float | None = None) -> dict[str, Any]:
        ms = self.receive(timeout=timeout)

        if ms is None:
            raise TimeoutError("No hay mensaje recibido en WebSocket")
        
        try:
            if isinstance(ms, str):
                return json.loads(ms)
            elif isinstance(ms, bytes):
                return json.loads(ms.decode('utf-8'))
            elif isinstance(ms, dict):
                return ms
            else:
                raise TypeError(f"Tipo de mensaje inesperado: {type(ms)}")
        except json.JSONDecodeError as e:
            logger.error(f"Error al decodificar JSON: {e}")
            logger.error(f"Mensaje recibido: {ms}")
            raise


    def clear_queue(self):
        while not self.incoming.empty(): # type: ignore
            try:
                self.incoming.get_nowait() # type: ignore
            except Empty:
                break
        logger.debug("Cola de mensajes limpiada")