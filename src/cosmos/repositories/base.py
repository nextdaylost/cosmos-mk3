"""Repository base."""


from typing import Generic, List, Type, TypeVar
from uuid import UUID

from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

from cosmos.core.models.base import ImmBase, OrmBase
from cosmos.db.exceptions import NotFoundException
from cosmos.db.session import SessionFactoryInjectable


CreateDtoT = TypeVar("CreateDtoT", bound=BaseModel)
ImmModelT = TypeVar("ImmModelT", bound=ImmBase)
OrmModelT = TypeVar("OrmModelT", bound=OrmBase)
UpdateDtoT = TypeVar("UpdateDtoT", bound=BaseModel)


class RepositoryBase(Generic[ImmModelT, OrmModelT, CreateDtoT, UpdateDtoT]):
    """Repository base.

    Attributes:
        _model: The in-memory model for the type being handled.
        _model_orm: The ORM for the type being handled.
        _session_factory: A database session factory.
    """

    def __init__(
        self,
        model: Type[ImmModelT],
        model_orm: Type[OrmModelT],
        session_factory: SessionFactoryInjectable,
    ):
        """Constructor.

        Args:
            model: The in-memory model for the type being handled.
            model_orm: The ORM for the type being handled.
            session_factory: A database session factory.
        """
        self._model = model
        self._model_orm = model_orm
        self._session_factory = session_factory

    def _create(self, session: Session, dto: CreateDtoT) -> OrmModelT:
        """Creates a persistent data object and returns its ORM.

        Used for intra-repository actions.

        Args:
            session: A database session.
            dto: Resource creation DTO.
        """
        obj_orm = self._model_orm(**dto.dict())
        session.add(obj_orm)
        return obj_orm

    def _delete_by_id(self, session: Session, resource_id: UUID) -> None:
        """Deletes a resource in the database.

        Args:
            session: A database session.
            resource_id: A resource id.
        """
        obj_orm = self._get_by_id(session, resource_id)
        session.delete(obj_orm)

    def _get_by_id(self, session: Session, resource_id: UUID) -> OrmModelT:
        """Retrieves persistent data object and returns its ORM.

        Used for intra-repository actions.

        Args:
            session: A database session.
            resource_id: A resource id.
        """
        row_tuple = session.execute(
            select(self._model_orm).where(self._model_orm.id == resource_id)
        ).first()
        if not row_tuple:
            raise NotFoundException(self._model, resource_id)
        return row_tuple[0]

    def create(self, dto: CreateDtoT) -> ImmModelT:
        """Creates a persistent data object and returns its in-memory model.

        Args:
            dto: Resource creation DTO.
        """
        with self._session_factory() as session:
            obj_orm = self._create(session, dto)
            session.commit()
            session.refresh(obj_orm)
            return self._model.from_orm(obj_orm)

    def delete_by_id(self, resource_id: UUID) -> None:
        """Deletes a resource in the database.

        Args:
            resource_id: A resource id.
        """
        with self._session_factory() as session:
            self._delete_by_id(session, resource_id)
            session.commit()

    def get_by_id(self, resource_id: UUID) -> ImmModelT:
        """Retrieves a resource from the database.

        Returns:
            A resource in its in-memory representation.
        """
        with self._session_factory() as session:
            obj_orm = self._get_by_id(session, resource_id)
            return self._model.from_orm(obj_orm)

    def list(self) -> List[ImmModelT]:
        """Retrieves a list of resources from the database.

        Returns:
            A list of resources in their in-memory representations.
        """
        with self._session_factory() as session:
            row_tuple_list = session.execute(select(self._model_orm)).all()
            return [self._model.from_orm(row_tuple[0]) for row_tuple in row_tuple_list]

    def update_by_id(self, resource_id: UUID, dto: UpdateDtoT) -> ImmModelT:
        """Updates a resource in the database.

        Args:
            resource_id: A resource id.
            dto: Resource update DTO.
        """
        with self._session_factory() as session:
            obj_orm = self._get_by_id(session, resource_id)
            for k, v in dto.dict().items():
                setattr(obj_orm, k, v)
            session.commit()
            session.refresh(obj_orm)
            return self._model.from_orm(obj_orm)
