import logging
from qdrant_client import QdrantClient, models
from app.application.ports.vector_store_port import VectorStorePort
from llama_index.core.vector_stores.types import BasePydanticVectorStore
from llama_index.vector_stores.qdrant import QdrantVectorStore # type: ignore
from app.shared.infrastructure_exceptions import VectorStoreException
from app.domain.entities.document import Document

logger = logging.getLogger(__name__)


class QdrantVectorStoreClient(VectorStorePort):
    def __init__(self, collection_name: str, url: str = "http://localhost:6333") -> None:
        self.collection_name = collection_name

        try:
            self._qdrant_client = QdrantClient(url=url)
            if not self._qdrant_client.collection_exists(
                collection_name=collection_name
            ):
                from qdrant_client.models import Distance, VectorParams

                self._colletion = self._qdrant_client.create_collection(
                    collection_name=collection_name,
                    vectors_config=VectorParams(size=768, distance=Distance.COSINE),
                )
        except Exception as e:
            raise VectorStoreException(
                "Error al conectar con Qdrant Vector store",
                collection=collection_name,
                details={"error": str(e)},
            )

    @property
    def get_vector_store(self) -> BasePydanticVectorStore:
        """Obtener Vector Store de LlamaIndex"""
        try:
            return QdrantVectorStore(
                collection_name=self.collection_name, client=self._qdrant_client
            )
        except Exception as e:
            raise VectorStoreException(
                "Error al build VectorStoreException",
                collection=self.collection_name,
                details={"error": str(e)},
            ) from e

    def query(self, query_text: str, top_k: int = 5) -> list[Document]:
        try:
            vector_store = self.get_vector_store

            from llama_index.core import VectorStoreIndex

            index = VectorStoreIndex.from_vector_store(vector_store)  # type: ignore
            retriever = index.as_retriever(similarity_top_k=top_k)

            nodes = retriever.retrieve(query_text)

            documents: list[Document] = []

            for node in nodes:
                document = Document(
                    id=int(node.node_id),
                    content=node.get_content(),
                    metadata=node.metadata,
                )
                documents.append(document)

            return documents
        except Exception as e:
            logger.error(f"Error en RAG query: {e}")
            raise VectorStoreException("Fallo en la recuperacion de contexto")

    def delete_documents(self, ids: list[str]) -> bool:
        """elimina puntos especificos por ID."""
        try:
            ids_int = [int(id_str) for id_str in ids]

            self._qdrant_client.delete(
                collection_name=self.collection_name, points_selector=models.PointIdsList(
                    points=ids_int # type: ignore
                )
            )
            return True
        except Exception as e:
            logger.error(f"Error eliminando puntos: {e}")
            raise VectorStoreException(
                "Error eliminando documentos",
                collection=self.collection_name,
                details={"ids": ids, "error": str(e)},
            ) from e

    def delete_collection(self) -> bool:
        try:
            self._qdrant_client.delete_collection(collection_name=self.collection_name)
            return True
        except Exception as e:
            logger.error(f"Error al borrar collection: {e}")
            raise VectorStoreException(
                "Error eliminando collection",
                collection=self.collection_name,
                details={"error": str(e)},
            ) from e
            

    def get_collection_count(self) -> int:
        try:
            collection_info = self._qdrant_client.get_collection(self.collection_name)
            
            if collection_info.points_count is None:
                logger.info("Vector es None")
                return 0

            return collection_info.points_count
        except Exception as e:
            raise VectorStoreException(
                f"Error obteniendo conteo de la Collection: {str(e)}",
                details={
                    "error": str(e)
                }
            )
