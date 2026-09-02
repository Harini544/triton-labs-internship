"""Tests for user endpoints."""

from fastapi.testclient import TestClient


def test_create_user(client: TestClient) -> None:
    response = client.post(
        "/users/",
        json={"name": "Asha Rao", "email": "asha@example.com"},
    )

    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Asha Rao"
    assert data["email"] == "asha@example.com"


def test_get_user(client: TestClient) -> None:
    created = client.post(
        "/users/",
        json={"name": "Asha Rao", "email": "asha@example.com"},
    ).json()

    response = client.get(f"/users/{created['id']}")

    assert response.status_code == 200
    assert response.json()["email"] == "asha@example.com"


def test_user_validation_rejects_invalid_email(client: TestClient) -> None:
    response = client.post(
        "/users/",
        json={"name": "Asha Rao", "email": "not-an-email"},
    )

    assert response.status_code == 422


def test_user_validation_rejects_short_name(client: TestClient) -> None:
    response = client.post("/users/", json={"name": "A", "email": "a@example.com"})

    assert response.status_code == 422
