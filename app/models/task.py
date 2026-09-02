"""Task domain model."""

from dataclasses import dataclass
from enum import Enum


class TaskStatus(str, Enum):
    """Allowed task status values."""

    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


@dataclass
class Task:
    """Internal representation of a task."""

    id: int
    title: str
    description: str | None
    status: TaskStatus
    user_id: int
