"""User management business logic."""

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.utils.id_generator import IdGenerator


class UserService:
    """Manage users using in-memory storage."""

    def __init__(self) -> None:
        self._users: dict[int, User] = {}
        self._id_generator = IdGenerator()

    def create_user(self, user_data: UserCreate) -> User:
        """Create and store a new user."""
        if self._email_exists(user_data.email):
            raise ValueError("Email is already registered")

        user_id = self._id_generator.next_id()
        user = User(id=user_id, name=user_data.name, email=str(user_data.email))
        self._users[user_id] = user
        return user

    def list_users(self) -> list[User]:
        """Return all stored users."""
        return list(self._users.values())

    def get_user(self, user_id: int) -> User | None:
        """Return a user by ID, if it exists."""
        return self._users.get(user_id)

    def update_user(self, user_id: int, user_data: UserUpdate) -> User | None:
        """Update an existing user and return it."""
        user = self.get_user(user_id)
        if user is None:
            return None

        if user_data.email is not None and self._email_exists(
            user_data.email,
            ignored_user_id=user_id,
        ):
            raise ValueError("Email is already registered")

        if user_data.name is not None:
            user.name = user_data.name
        if user_data.email is not None:
            user.email = str(user_data.email)

        return user

    def delete_user(self, user_id: int) -> bool:
        """Delete a user by ID."""
        return self._users.pop(user_id, None) is not None

    def reset(self) -> None:
        """Clear storage. Intended for tests."""
        self._users.clear()
        self._id_generator.reset()

    def _email_exists(self, email: str, ignored_user_id: int | None = None) -> bool:
        normalized_email = str(email).lower()
        return any(
            user.email.lower() == normalized_email and user.id != ignored_user_id
            for user in self._users.values()
        )


user_service = UserService()
