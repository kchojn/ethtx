from typing import List

from ethtx.events.observer.observer_abc import Observer
from ethtx.events.observer.subject_abc import Subject


class EventSubject(Subject):
    _current_event_state: str = None

    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self, observer: Observer) -> None:
        for observer in self._observers:
            observer.update(self)
