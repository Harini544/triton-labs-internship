"""Task management business logic."""

from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate
from app.utils.id_generator import IdGenerator


class TaskService:
    """Manage tasks using in-memory storage."""

    def __init__(self) -> None:
        self._tasks: dict[int, Task] = {}
        self._id_generator = IdGenerator()

    def create_task(self, task_data: TaskCreate) -> Task:
        """Create and store a new task."""
        task_id = self._id_generator.next_id()
        task = Task(
            id=task_id,
            title=task_data.title,
            description=task_data.description,
            status=task_data.status,
            user_id=task_data.user_id,
        )
        self._tasks[task_id] = task
        return task

    def list_tasks(self) -> list[Task]:
        """Return all stored tasks."""
        return list(self._tasks.values())

    def get_task(self, task_id: int) -> Task | None:
        """Return a task by ID, if it exists."""
        return self._tasks.get(task_id)

    def update_task(self, task_id: int, task_data: TaskUpdate) -> Task | None:
        """Update an existing task and return it."""
        task = self.get_task(task_id)
        if task is None:
            return None

        if task_data.title is not None:
            task.title = task_data.title
        if "description" in task_data.model_fields_set:
            task.description = task_data.description
        if task_data.status is not None:
            task.status = task_data.status
        if task_data.user_id is not None:
            task.user_id = task_data.user_id

        return task

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by ID."""
        return self._tasks.pop(task_id, None) is not None

    def delete_tasks_for_user(self, user_id: int) -> None:
        """Delete all tasks owned by a user."""
        task_ids = [
            task_id
            for task_id, task in self._tasks.items()
            if task.user_id == user_id
        ]
        for task_id in task_ids:
            self.delete_task(task_id)

    def reset(self) -> None:
        """Clear storage. Intended for tests."""
        self._tasks.clear()
        self._id_generator.reset()


task_service = TaskService()
