import pytest
from app.services.rag_service import get_rag_response

@pytest.mark.asyncio
async def test_rag_response():
    response = await get_rag_response("What is insurance liability?")
    assert isinstance(response, dict)
    assert "answer" in response
    assert isinstance(response["citations"], list)