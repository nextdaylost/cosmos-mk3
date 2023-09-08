"""Application entrypoint."""


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

    if settings.cors_origins:
        app.add_middleware(
            CORSMiddleware,
            allow_credentials=True,
            allow_headers=["*"],
            allow_methods=["*"],
            allow_origins=[str(origin) for origin in settings.cors_origins],
        )

    return app
