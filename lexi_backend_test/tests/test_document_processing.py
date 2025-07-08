from app.services.document_loader import initialize_documents
from app.services.embedding_service import get_vector_store

def test_document_loading():
    initialize_documents()
    vector_store = get_vector_store()
    assert vector_store.index.ntotal > 0  # Verify documents were embedded