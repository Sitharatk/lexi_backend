import os
import requests
from langchain.document_loaders import (
    DirectoryLoader,
    UnstructuredPDFLoader,
    UnstructuredWordDocumentLoader
)
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.config import settings
from app.services.embedding_service import init_vector_store

async def initialize_documents():
    """Load and process documents into vector store"""
    if not os.path.exists(settings.DOCUMENTS_DIR):
        os.makedirs(settings.DOCUMENTS_DIR)
        await download_sample_documents()

    loader = DirectoryLoader(
        settings.DOCUMENTS_DIR,
        glob="**/*.*",
        loader_cls=lambda path: (
            UnstructuredWordDocumentLoader(path) if path.endswith(".docx") 
            else UnstructuredPDFLoader(path)
        )
    )
    
    documents = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.CHUNK_SIZE,
        chunk_overlap=settings.CHUNK_OVERLAP
    )
    chunks = text_splitter.split_documents(documents)
    
    await init_vector_store(chunks)

async def download_sample_documents():
    """Download sample legal documents if none exist"""
    doc_urls = [
        "https://www.supremecourt.gov/opinions/22pdf/21-376_6537.pdf",
        "https://www.uscourts.gov/sites/default/files/pattern_criminal_0.docx"
    ]
    
    for url in doc_urls:
        try:
            response = requests.get(url)
            response.raise_for_status()
            filename = os.path.join(
                settings.DOCUMENTS_DIR,
                os.path.basename(url)
            )
            with open(filename, 'wb') as f:
                f.write(response.content)
        except Exception as e:
            print(f"Failed to download document: {str(e)}")