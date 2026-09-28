from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_create_task():

    response = client.post(
        "/tasks/",
        json={
            "title": "Test Task",
            "description": "Created through pytest",
            "priority": 3
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "Test Task"
    assert data["description"] == "Created through pytest"
    assert data["priority"] == 3
    assert data["status"] == "pending"