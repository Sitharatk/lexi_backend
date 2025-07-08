from pydantic import BaseModel
from typing import List, Optional

class Citation(BaseModel):
    text: str
    source: str
    page_number: Optional[int] = None

class QueryResponse(BaseModel):
    answer: str
    citations: List[Citation]

class QueryRequest(BaseModel):
    query: str