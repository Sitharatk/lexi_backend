from langchain.chains import RetrievalQA
from langchain.llms import HuggingFaceHub
from app.config import settings
from app.services.embedding_service import get_vector_store
from app.models import QueryResponse, Citation

qa_chain = None

async def initialize_rag():
    """Initialize the RAG pipeline"""
    global qa_chain
    vector_store = get_vector_store()
    
    llm = HuggingFaceHub(
        repo_id=settings.LLM_REPO_ID,
        model_kwargs={
            "temperature": 0.1,
            "max_length": 1024
        }
    )
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever(),
        return_source_documents=True
    )

async def get_rag_response(query: str) -> QueryResponse:
    """Get RAG response for a query"""
    if not qa_chain:
        await initialize_rag()
    
    result = qa_chain({"query": query})
    
    citations = [
        Citation(
            text=doc.page_content,
            source=os.path.basename(doc.metadata.get("source", "unknown")),
            page_number=doc.metadata.get("page_number")
        )
        for doc in result.get("source_documents", [])
    ]
    
    return QueryResponse(
        answer=result.get("result", "No answer generated"),
        citations=citations
    )