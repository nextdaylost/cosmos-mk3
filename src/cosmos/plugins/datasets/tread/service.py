"""Tread query service."""


from typing import Annotated

from fastapi import Depends

from cosmos.core.models.dataset import (
    Dataset,
    DatasetCreateDto,
    DatasetOrm,
    DatasetUpdateDto,
)
from cosmos.db.session import SessionFactoryInjectable
from cosmos.repositories.base import RepositoryBase


class TreadQueryService:
    """Handles persistence operations for dataset objects."""

    def __init__(self, session_factory: SessionFactoryInjectable):
        """Constructor.

        Args:
            session_factory: A database session factory.
        """
        super().__init__(
            session_factory=session_factory,
        )


DatasetRepositoryInjectable = Annotated[DatasetRepository, Depends(DatasetRepository)]
