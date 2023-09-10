"""Application base models."""


from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel
from sqlalchemy import Column, DateTime, Uuid
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.sql.functions import func

from cosmos.utils.string import to_camel


class ImmBase(BaseModel):
    """Global base class for in-memory data objects.

    Attributes:
        id: A globally unique identifier.
        created_at: A timestamp of creation.
        updated_at: A timestamp of last update.
    """

    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        """Pydantic BaseModel-specific configuration.

        See Pydantic documentation for more information.
        """

        alias_generator = to_camel
        allow_population_by_field_name = True
        orm_mode = True


@as_declarative()
class OrmBase:
    """Global base class for data persistence objects.

    Attributes:
        id: A globally unique identifier.
        created_at: A timestamp of creation.
        updated_at: A timestamp of last update.
    """

    __abstract__ = True

    id = Column(Uuid, primary_key=True, nullable=False, default=uuid4)
    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.current_timestamp(),
    )
    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.current_timestamp(),
        onupdate=func.current_timestamp(),
        server_onupdate=func.current_timestamp(),
    )
