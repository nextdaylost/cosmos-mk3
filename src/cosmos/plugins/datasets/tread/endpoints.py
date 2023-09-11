"""Tread path operations."""


from uuid import UUID

from fastapi import APIRouter, status

from cosmos.repositories.dataset import DatasetRepositoryInjectable


router = APIRouter()


@router.get("/{dataset_id}/q", status_code=status.HTTP_200_OK)
def query(dataset_id: UUID, dataset_repository: DatasetRepositoryInjectable):
    """Executes a query."""
    dataset = dataset_repository.get_by_id(dataset_id)
    return f"Querying {dataset.name}"
