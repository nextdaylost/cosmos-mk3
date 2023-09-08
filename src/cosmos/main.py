"""Application entrypoint."""


from fastapi import FastAPI

from cosmos.metadata import __version__


def main() -> FastAPI:
    """Application factory.

    Returns:
        An initialized FastAPI application instance.
    """
    app = FastAPI(version=__version__)

    return app
