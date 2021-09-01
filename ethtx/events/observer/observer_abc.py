from abc import ABC, abstractmethod


class Observer(ABC):
    """ The Observer interface declares the update method, used by subjects. """

    @abstractmethod
    def update(self, subject, *args, **kwargs) -> None:
        """ Receive update from subject. """
        ...
