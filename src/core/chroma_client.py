import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore


class Chroma:
    def __init__(self, collection: str, path_db: str = "./chroma_db"):
        self.path_db = path_db
        self.collection = collection

    def createClientDb(self):
        chroma_client = chromadb.PersistentClient(path=self.path_db)
        return chroma_client

    def createChromaCollection(self):
        chroma_collection = self.createClientDb().get_or_create_collection(
            self.collection
        )
        return chroma_collection

    def vectorStore(self):
        vector_store = ChromaVectorStore(
            chroma_collection=self.createChromaCollection()
        )
        return vector_store
