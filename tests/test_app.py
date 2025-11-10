import pytest
from ACEest_Fitness import app

@pytest.fixture
def client():
    return app.test_client()

def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json["status"] == "healthy"

def test_classes(client):
    resp = client.get("/classes")
    assert resp.status_code == 200
    assert "Yoga" in resp.json["classes"]

def test_membership(client):
    resp = client.get("/membership")
    assert resp.status_code == 200
    assert any(plan["type"] == "Premium" for plan in resp.json["plans"])
