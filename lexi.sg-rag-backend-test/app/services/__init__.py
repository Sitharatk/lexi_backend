# Initialize services package
from .document_loader import initialize_documents
from .rag_service import get_rag_response

__all__ = ["initialize_documents", "get_rag_response"]