import time
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
    def notify(self) -> None:
        """ Notify all observers about the event. """
        ...

    @abstractmethod
    def notify_start(self, starts: time.time) -> None:
        """ Notify all observers about the start the event. """
        ...

    @abstractmethod
    def notify_end(self, ends: time.time) -> None:
        """ Notify all observers about the end of the event. """
        ...
