
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.config import settings

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def sample_query():
    return {"query": "What is insurance liability?"}

@pytest.fixture
def mock_documents():
    return [
        {
            "page_content": "Insurance liability depends on the permit status.",
            "metadata": {"source": "doc1.pdf"}
        }
    ]