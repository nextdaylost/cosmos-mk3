"""Dataset path operations."""


from uuid import UUID

from fastapi import APIRouter, Response, status

from cosmos.core.models.dataset import (
    DatasetCreateDto,
    DatasetUpdateDto,
)
from cosmos.db.exceptions import NotFoundException
from cosmos.repositories.dataset import DatasetRepositoryInjectable


router = APIRouter(prefix="/datasets")


@router.post("", status_code=status.HTTP_201_CREATED)
def create_dataset(
    dataset_dto: DatasetCreateDto,
    dataset_repository: DatasetRepositoryInjectable,
):
    """Creates a dataset.

    Args:
        dataset_dto: A dataset creation DTO.
        dataset_repository: Dataset repository.
    """
    return dataset_repository.create(dataset_dto)


@router.delete("/{dataset_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_dataset(dataset_id: UUID, dataset_repository: DatasetRepositoryInjectable):
    """Deletes a dataset.

    Args:
        dataset_id: A dataset id.
        dataset_repository: Dataset repository.
    """
    try:
        dataset_repository.delete_by_id(dataset_id)
    except NotFoundException:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.get("/{dataset_id}", status_code=status.HTTP_200_OK)
def get_dataset(dataset_id: UUID, dataset_repository: DatasetRepositoryInjectable):
    """Retrieves a dataset.

    Args:
        dataset_id: A dataset id.
        dataset_repository: Dataset repository.
    """
    try:
        return dataset_repository.get_by_id(dataset_id)
    except NotFoundException:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.get("", status_code=status.HTTP_200_OK)
def list_datasets(dataset_repository: DatasetRepositoryInjectable):
    """Lists datasets.

    Args:
        dataset_repository: Dataset repository.
    """
    return dataset_repository.list()


@router.patch("/{dataset_id}", status_code=status.HTTP_200_OK)
def update_dataset(
    dataset_id: UUID,
    dataset_dto: DatasetUpdateDto,
    dataset_repository: DatasetRepositoryInjectable,
):
    """Updates a dataset.

    Args:
        dataset_id: A dataset id.
        dataset_dto: A dataset update DTO.
        dataset_repository: Dataset repository.
    """
    return dataset_repository.update_by_id(dataset_id, dataset_dto)
