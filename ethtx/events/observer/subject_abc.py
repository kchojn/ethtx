from abc import ABC, abstractmethod

from ethtx.events.observer.observer_abc import Observer


class Subject(ABC):
    """ The Subject interface declares a set of methods for managing subscribers. """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """  Attach an observer to the subject. """
        ...

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """ Detach an observer from the subject. """
        ...

    @abstractmethod
    def notify(self, observer: Observer) -> None:
        """ Notify all observers about an event. """
        ...
