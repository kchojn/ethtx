from abc import ABC, abstractmethod


class Observer(ABC):
    """ The Observer interface declares the update method, used by subjects. """

    def __repr__(self) -> str:
        return self.__str__()

    @abstractmethod
    def update(self, subject, *args, **kwargs) -> None:
        """ Receive update from subject. """
        ...
