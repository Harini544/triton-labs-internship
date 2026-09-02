"""User request and response schemas."""

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserBase(BaseModel):
    """Shared user fields."""

    name: str = Field(..., min_length=2, max_length=80)
    email: EmailStr


class UserCreate(UserBase):
    """Schema for creating a user."""


class UserUpdate(BaseModel):
    """Schema for updating a user."""

    name: str | None = Field(default=None, min_length=2, max_length=80)
    email: EmailStr | None = None


class UserResponse(UserBase):
    """Schema returned by user endpoints."""

    id: int

    model_config = ConfigDict(from_attributes=True)
