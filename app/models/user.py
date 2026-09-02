"""User domain model."""

from dataclasses import dataclass


@dataclass
class User:
    """Internal representation of a user."""

    id: int
    name: str
    email: str
