"""Ping utility."""


from fastapi import APIRouter, Response, status


router = APIRouter(prefix="/ping")


@router.get("", include_in_schema=False)
async def ping():
    """Ping path operation.

    Responds with 200 OK to GET requests. Helps confirm the application is
    reachable and debug networking issues. Can serve as a heartbeat mechanism for
    load balancer health checks.
    """
    return Response(status_code=status.HTTP_200_OK)
