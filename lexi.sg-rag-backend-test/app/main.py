from fastapi import FastAPI, HTTPException
from app.models import QueryRequest, QueryResponse
from app.services.rag_service import get_rag_response
from app.services.document_loader import initialize_documents
import os

app = FastAPI(
    title="Lexi.sg RAG Backend",
    description="Retrieval-Augmented Generation for Legal Queries",
    version="1.0.0"
)

@app.on_event("startup")
async def startup_event():
    """Initialize document processing and RAG system"""
    if not os.path.exists("data/documents"):
        os.makedirs("data/documents")
    await initialize_documents()

@app.post("/query", response_model=QueryResponse)
async def process_query(request: QueryRequest):
    """Process legal queries with RAG"""
    try:
        return await get_rag_response(request.query)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "lexi-rag"}