"""Database errors."""


from typing import Type, TypeVar
from uuid import UUID


ResourceT = TypeVar("ResourceT")


class NotFoundException(Exception):
    """Resource not found exception."""

    def __init__(self, resource_type: Type[ResourceT], resource_id: UUID):
        """Constructor.

        Args:
            resource_type: The type of resource being accessed.
            resource_id: The id of the resources being accessed.
        """
        super().__init__(f"{resource_type.__name__} '{resource_id}' not found.")
