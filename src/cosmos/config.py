"""Application settings and configuration."""


from typing import List, Literal, Optional

from pydantic import AnyHttpUrl, BaseSettings, constr


_api_prefix = constr(regex=r"^$|^/[a-zA-Z0-9\-\.\_\~]+$")


class OpenApiInfo(BaseSettings):
    """OpenAPI Info object.

    Attributes:
        title: The title of the API.
        description: A description of the API. Accepts CommonMark syntax.
        summary: A short summary of the API.
    """

    title: str = "Cosmos"
    description: Optional[str] = None
    summary: Optional[str] = "A system for processing, storing, and sharing data"


class Settings(BaseSettings):
    """Root application settings.

    Attributes:
        api_prefix: The API path prefix.
        cors_origins: A list of trusted URLs for cross-origin requests.
        env: The runtime environment.
        openapi: An OpenApiInfo object.
    """

    api_prefix: _api_prefix = ""
    cors_origins: List[AnyHttpUrl] = []
    env: Literal["dev", "prod"] = "dev"
    openapi: OpenApiInfo = OpenApiInfo()

    class Config:
        """Pydantic BaseSettings-specific configuration.

        See Pydantic documentation for more information.
        """

        env_nested_delimiter = "__"
        env_prefix = "COSMOS_"


settings = Settings()
