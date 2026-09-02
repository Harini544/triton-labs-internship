"""Small utility for sequential in-memory IDs."""


class IdGenerator:
    """Generate simple increasing integer IDs."""

    def __init__(self) -> None:
        self._next_id = 1

    def next_id(self) -> int:
        """Return the next available ID."""
        current_id = self._next_id
        self._next_id += 1
        return current_id

    def reset(self) -> None:
        """Reset ID generation back to the first ID."""
        self._next_id = 1
