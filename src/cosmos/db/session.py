"""Database session."""


from contextlib import AbstractContextManager, contextmanager
from typing import Annotated, Callable, Generator

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, Session, sessionmaker

from cosmos.config import settings


engine = create_engine(settings.sqlalchemy_url)
session_factory = scoped_session(sessionmaker(autoflush=False, bind=engine))


def create_session() -> Generator[Session, None, None]:
    """Creates a database session.

    Yields:
        A database session.
    """
    session = session_factory()
    try:
        yield session
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


SessionFactoryInjectable = Annotated[
    Callable[..., AbstractContextManager[Session]],
    Depends(lambda: contextmanager(create_session)),
]
