import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Test that the homepage loads successfully and returns expected welcome message."""
    response = client.get("/")
    assert response.status_code == 200
    json_data = response.get_json()
    assert "message" in json_data
    assert "Personal Movie Watchlist Tracker" in json_data["message"]

def test_watchlist_route(client):
    """Test that the /watchlist endpoint returns movies with proper keys."""
    response = client.get("/watchlist")
    assert response.status_code == 200
    json_data = response.get_json()
    assert "movies" in json_data
    assert "total_movies" in json_data
    assert json_data["total_movies"] == len(json_data["movies"])
    assert len(json_data["movies"]) > 0
    # Check structure of the first movie item
    movie = json_data["movies"][0]
    assert "id" in movie
    assert "title" in movie
    assert "genre" in movie
    assert "year" in movie

def test_top_pick_route(client):
    """Test that the /top-pick endpoint returns tonight's featured movie."""
    response = client.get("/top-pick")
    assert response.status_code == 200
    json_data = response.get_json()
    assert "recommendation" in json_data
    assert "title" in json_data["recommendation"]
    assert "note" in json_data

def test_health_check_route(client):
    """Test that the /health endpoint returns status: healthy."""
    response = client.get("/health")
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data == {"status": "healthy"}
