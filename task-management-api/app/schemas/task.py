"""Task request and response schemas."""

from pydantic import BaseModel, ConfigDict, Field

from app.models.task import TaskStatus


class TaskBase(BaseModel):
    """Shared task fields."""

    title: str = Field(..., min_length=3, max_length=100)
    description: str | None = Field(default=None, max_length=500)
    status: TaskStatus = TaskStatus.TODO
    user_id: int = Field(..., gt=0)


class TaskCreate(TaskBase):
    """Schema for creating a task."""


class TaskUpdate(BaseModel):
    """Schema for updating a task."""

    title: str | None = Field(default=None, min_length=3, max_length=100)
    description: str | None = Field(default=None, max_length=500)
    status: TaskStatus | None = None
    user_id: int | None = Field(default=None, gt=0)


class TaskResponse(TaskBase):
    """Schema returned by task endpoints."""

    id: int

    model_config = ConfigDict(from_attributes=True)
