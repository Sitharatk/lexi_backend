def test_query_endpoint(client, sample_query):
    response = client.post("/query", json=sample_query)
    assert response.status_code == 200
    assert "answer" in response.json()
    assert "citations" in response.json()

def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "service": "lexi-rag"}