"""Task API routes."""

from fastapi import APIRouter, HTTPException, status

from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from app.services.task_service import task_service
from app.services.user_service import user_service

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate) -> TaskResponse:
    """Create a new task for an existing user."""
    if user_service.get_user(task_data.user_id) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return TaskResponse.model_validate(task_service.create_task(task_data))


@router.get("/", response_model=list[TaskResponse])
def list_tasks() -> list[TaskResponse]:
    """Return all tasks."""
    return [TaskResponse.model_validate(task) for task in task_service.list_tasks()]


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int) -> TaskResponse:
    """Return a task by ID."""
    task = task_service.get_task(task_id)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )
    return TaskResponse.model_validate(task)


@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_data: TaskUpdate) -> TaskResponse:
    """Update an existing task."""
    if task_data.user_id is not None and user_service.get_user(task_data.user_id) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    task = task_service.update_task(task_id, task_data)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )
    return TaskResponse.model_validate(task)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> None:
    """Delete a task by ID."""
    deleted = task_service.delete_task(task_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )
