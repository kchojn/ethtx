from abc import ABC, abstractmethod
from typing import List, Union

from ethtx.events.observer.observer_abc import Observer


class Subject(ABC):
    """ The Subject interface declares a set of methods for managing subscribers. """

    @abstractmethod
    def attach(self, observer: Union[Observer, List[Observer]]) -> None:
        """  Attach an observer to the subject. """
        ...

    @abstractmethod
    def detach(self, observer: Union[Observer, List[Observer]]) -> None:
        """ Detach an observer from the subject. """
        ...

    @abstractmethod
    def notify(self, observers: Union[Observer, List[Observer]], **kwargs) -> None:
        """ Notify all observers about an event. """
        ...