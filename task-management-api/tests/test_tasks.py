"""Tests for task endpoints."""

from fastapi.testclient import TestClient


def create_user(client: TestClient) -> dict:
    response = client.post(
        "/users/",
        json={"name": "Asha Rao", "email": "asha@example.com"},
    )
    return response.json()


def test_create_task(client: TestClient) -> None:
    user = create_user(client)

    response = client.post(
        "/tasks/",
        json={
            "title": "Write README",
            "description": "Document setup and API usage.",
            "status": "todo",
            "user_id": user["id"],
        },
    )

    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "Write README"
    assert data["user_id"] == user["id"]


def test_get_task(client: TestClient) -> None:
    user = create_user(client)
    created = client.post(
        "/tasks/",
        json={"title": "Review code", "user_id": user["id"]},
    ).json()

    response = client.get(f"/tasks/{created['id']}")

    assert response.status_code == 200
    assert response.json()["title"] == "Review code"


def test_task_validation_rejects_short_title(client: TestClient) -> None:
    user = create_user(client)

    response = client.post("/tasks/", json={"title": "No", "user_id": user["id"]})

    assert response.status_code == 422


def test_task_requires_existing_user(client: TestClient) -> None:
    response = client.post(
        "/tasks/",
        json={"title": "Plan sprint", "user_id": 999},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"
