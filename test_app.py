import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Test that the homepage HTML loads successfully and contains the branding."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Personal Movie Watchlist Tracker" in response.data
    assert b"DevOps Pipeline:" in response.data

def test_watchlist_route(client):
    """Test that the /watchlist endpoint renders HTML movie cards."""
    response = client.get("/watchlist")
    assert response.status_code == 200
    assert b"My Planned Watchlist" in response.data
    assert b"Inception" in response.data
    assert b"The Dark Knight" in response.data
    assert b"Interstellar" in response.data

def test_top_pick_route(client):
    """Test that the /top-pick endpoint renders the featured recommendation card."""
    response = client.get("/top-pick")
    assert response.status_code == 200
    assert b"Tonight's Top Pick" in response.data
    assert b"Inception" in response.data
    assert b"Featured Recommendation" in response.data

def test_health_check_route(client):
    """Test that the /health endpoint returns JSON status: healthy."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}
