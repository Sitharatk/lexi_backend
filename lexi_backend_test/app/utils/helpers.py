import os
from typing import List

def validate_documents_dir(path: str) -> bool:
    """Check if documents directory contains valid files"""
    if not os.path.exists(path):
        return False
    return any(
        f.endswith(('.pdf', '.docx')) 
        for f in os.listdir(path)
    )

def get_document_list() -> List[str]:
    """List available documents"""
    from app.config import settings
    return [
        f for f in os.listdir(settings.DOCUMENTS_DIR)
        if f.endswith(('.pdf', '.docx'))
    ]