"""Application entrypoint."""


from fastapi import FastAPI

from cosmos.config import settings
from cosmos.metadata import __version__


def main() -> FastAPI:
    """Application factory.

    Returns:
        An initialized FastAPI application instance.
    """
    app = FastAPI(
        description=settings.openapi.description,
        summary=settings.openapi.summary,
        title=settings.openapi.title,
        version=__version__,
    )

    return app
