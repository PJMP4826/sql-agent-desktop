from app.application.ports.rag_client_port import RagClientPort
from app.infrastructure.websocket.websocket_client import WebSocketClient
from app.shared.infrastructure_exceptions import InfrastructureException
import logging

logger = logging.getLogger(__name__)

class RagClientService(RagClientPort):
    def __init__(self, ws_client: WebSocketClient) -> None:
        self._ws_client = ws_client
        self._is_initialized = False

    def connect_server(self, timeout: float = 10.0):
        """
        Conecta al servidor RAG WebSocket.
        
        Args:
            timeout: Tiempo maximo de espera para la conexion
            
        Raises:
            InfrastructureException: Si no puede conectar
        """
        if self._is_initialized and self._ws_client.is_connected():
            logger.warning("El cliente ya esta conectado")
            return

        self._ws_client.start()

        # esperar a que se conecte
        if not self._ws_client.wait_for_connection(timeout=timeout):
            raise InfrastructureException("No se pudo conectar al servidor RAG")

        self._is_initialized = True

    def disconnect(self):
        if self._ws_client:
            logger.info("Desconectando del servidor RAG")
            self._ws_client.stop()
            self._is_initialized = False

    def _ensure_connected(self, timeout: float = 5.0):
        if not self._is_initialized:
            self.connect_server(timeout=timeout)
        elif not self._ws_client.is_connected():
            logger.warning("Conexión perdida, reconectando")
            self.connect_server(timeout=timeout)
        
    def query(self, query: str, timeout: float = 30.0) -> str:
        try:
            # asegurar que hay conexion
            self._ensure_connected()
            
            self._ws_client.send(message=query)
            
            result = self._ws_client.receive(timeout=timeout)
            
            if result is None:
                raise InfrastructureException(
                    f"No se recibio respuesta del servidor RAG en {timeout}s"
                )
            
            return str(result)
        except InfrastructureException:
            raise
        except Exception as e:
            logger.error(f"Error al consultar el servidor RAG: {e}")
            raise InfrastructureException(
                f"Error al consultar el servidor RAG: {str(e)}"
            )
        
    def chat(self, question: str, timeout: float = 30.0) -> str:
        return self.query(question, timeout=timeout)

    async def async_query(self, query: str) -> str:
        raise NotImplementedError("async_query no esta implementado")
    
    async def async_chat(self, question: str) -> str:
        raise NotImplementedError("async_chat no esta implementado")

    def __enter__(self):
        self.connect_server()
        return self