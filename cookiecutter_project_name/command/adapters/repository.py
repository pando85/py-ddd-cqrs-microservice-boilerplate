import abc
from uuid import UUID

from cookiecutter_project_name.command.domain.models import Pet


class Repository(abc.ABC):
    """The repository interface for the Pet aggregate"""

    @abc.abstractmethod
    def get_by_id(self, id: UUID) -> Pet:
        """
        Get a Pet by id.

        :param id: the pet's identifier
        :return: the pet
        """
        raise NotImplementedError

    @abc.abstractmethod
    def add(self, pet: Pet) -> UUID:
        """
        Add a Pet to the repository.

        :param pet: Pet the pet to add
        :return: the id of the added pet.
        """
        raise NotImplementedError