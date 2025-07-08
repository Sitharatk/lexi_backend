from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from app.config import settings

vector_store = None

async def init_vector_store(documents):
    """Initialize the FAISS vector store with documents"""
    global vector_store
    embeddings = HuggingFaceEmbeddings(
        model_name=settings.EMBEDDING_MODEL
    )
    vector_store = FAISS.from_documents(documents, embeddings)
    return vector_store

def get_vector_store():
    """Get the initialized vector store"""
    if not vector_store:
        raise ValueError("Vector store not initialized")
    return vector_store