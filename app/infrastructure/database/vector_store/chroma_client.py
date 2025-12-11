import chromadb
import logging
from typing import List
from app.application.ports.vector_store_port import VectorStorePort
from app.domain.entities.document import Document
from llama_index.vector_stores.chroma import ChromaVectorStore # type: ignore

logger = logging.getLogger(__name__)


class ChromaClient(VectorStorePort):

    def __init__(
        self, collection_name: str, persist_directory: str = "./chroma_db"
    ) -> None:
        self.persist_directory = persist_directory
        self.collection_name = collection_name
        self._chroma_client = chromadb.PersistentClient(path=self.persist_directory)
        self._collection = self._chroma_client.get_or_create_collection(
            self.collection_name
        )

    @property
    def get_vector_store(self):
        """
        Obtener Vector Store de LlamaIndex
        """
        return ChromaVectorStore(chroma_collection=self._collection)

    def add_documents(self, documents: List[Document]) -> List[str]:
        try:
            ids: List[str] = [str(doc.id) for doc in documents]
            contents = [doc.content for doc in documents]
            # metadatas = [doc.metadata or {} for doc in documents]

            self._collection.add(ids=ids, documents=contents)
            logging.info(f"Add document {len(documents)} a chromaDb")

            return ids
        except Exception as e:
            logger.error(f"Error adding documents: {e}")
            raise

    def query(self, query_text: str, top_k: int = 5) -> List[Document]:
        try:
            results = self._collection.query(query_texts=[query_text], n_results=top_k)
            documents: List[Document] = []
            for i, doc_id in enumerate(results['ids'][0]):
                documents.append(Document(
                    id=int(doc_id),
                    content=results['documents'][0][i] if results['documents'] and len(results['documents']) > 0 else "",
                    metadata=dict(results['metadatas'][0][i]) if results['metadatas'] else {}
                ))
            return documents
        except Exception as e:
            logger.error(f"Error querying documents: {e}")
            raise

    def delete_collection(self) -> bool:
        try:
            self._chroma_client.delete_collection(self.collection_name)
            self._collection = self._chroma_client.get_or_create_collection(
                self.collection_name
            )
            return True
        except Exception as e:
            logger.error(f"Error deleting collection: {e}")
            return False

    def delete_documents(self, ids: List[str]) -> bool:
        try:
            self._collection.delete(ids=ids)
            logging.info(f"Deleted {len(ids)} documents")
            return True
        except Exception as e:
            logging.error(f"Error eliminando documentos {e}")
            return False
        
    def get_collection_count(self) -> int:
        return self._collection.count()
