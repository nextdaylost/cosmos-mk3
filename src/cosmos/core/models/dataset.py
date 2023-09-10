"""Dataset models."""


from typing import Optional

from pydantic import BaseModel
from sqlalchemy import Column, Text

from cosmos.core.models.base import ImmBase, OrmBase


class Dataset(ImmBase):
    """Dataset metadata object.

    name: Name of a dataset.
    """

    name: str


class DatasetCreateDto(BaseModel):
    """Dataset representation as transferred from the client prior to creation.

    name: Name of a dataset.
    """

    name: str


class DatasetUpdateDto(BaseModel):
    """Dataset representation as transferred from the client prior to update.

    name: Name of a dataset.
    """

    name: Optional[str]


class DatasetOrm(OrmBase):
    """Dataset object-relational mapping.

    name: Name of a dataset.
    """

    __tablename__ = "dataset"

    name = Column(Text, nullable=False)
