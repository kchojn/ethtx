from abc import ABC, abstractmethod

from ethtx.events.observer.subject_abc import Subject


class Observer(ABC):
    """ The Observer interface declares the update method, used by subjects. """

    def __str__(self) -> str:
        return f"Observer {self.__class__.__name__}(id:{id(self)})"

    def __repr__(self) -> repr:
        return self.__str__()

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """ Receive update from subject. """
        ...
