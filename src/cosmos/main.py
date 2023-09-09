"""Application entrypoint."""


from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from cosmos.config import settings
from cosmos.metadata import __version__
from cosmos.utils.endpoints import ping


def main() -> FastAPI:
    """Application factory.

    Returns:
        An initialized FastAPI application instance.
    """
    app = FastAPI(
        description=settings.openapi.description,
        openapi_url=f"{settings.api_prefix}/openapi.json",
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

    router = APIRouter(prefix=settings.api_prefix)

    router.include_router(ping.router)

    app.include_router(router)

    return app
