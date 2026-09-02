"""FastAPI application entry point."""

from fastapi import FastAPI

from app.config import settings
from app.routers import tasks, users

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="A beginner-friendly modular Task Management API.",
)

app.include_router(users.router)
app.include_router(tasks.router)


@app.get("/health", tags=["Health"])
def health_check() -> dict[str, str]:
    """Return API health status."""
    return {"status": "ok"}
