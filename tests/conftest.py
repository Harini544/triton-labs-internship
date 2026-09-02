"""Shared pytest fixtures."""

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.services.task_service import task_service
from app.services.user_service import user_service


@pytest.fixture(autouse=True)
def reset_services() -> None:
    """Start each test with empty in-memory storage."""
    user_service.reset()
    task_service.reset()


@pytest.fixture
def client() -> TestClient:
    """Return a FastAPI test client."""
    return TestClient(app)
