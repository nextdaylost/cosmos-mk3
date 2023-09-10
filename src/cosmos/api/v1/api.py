"""API v1 router.

Aggregates path operations for API v1.
"""


from fastapi import APIRouter

from cosmos.api.v1.endpoints import datasets


router = APIRouter(prefix="/v1")

router.include_router(datasets.router)
