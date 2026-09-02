"""User API routes."""

from fastapi import APIRouter, HTTPException, status

from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.services.task_service import task_service
from app.services.user_service import user_service

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserCreate) -> UserResponse:
    """Create a new user."""
    try:
        user = user_service.create_user(user_data)
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error),
        ) from error
    return UserResponse.model_validate(user)


@router.get("/", response_model=list[UserResponse])
def list_users() -> list[UserResponse]:
    """Return all users."""
    return [UserResponse.model_validate(user) for user in user_service.list_users()]


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int) -> UserResponse:
    """Return a user by ID."""
    user = user_service.get_user(user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return UserResponse.model_validate(user)


@router.patch("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_data: UserUpdate) -> UserResponse:
    """Update an existing user."""
    try:
        user = user_service.update_user(user_id, user_data)
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error),
        ) from error

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return UserResponse.model_validate(user)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int) -> None:
    """Delete a user by ID."""
    deleted = user_service.delete_user(user_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    task_service.delete_tasks_for_user(user_id)
