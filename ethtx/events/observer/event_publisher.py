from typing import List

from ethtx.events.observer.const import EventCollection
from ethtx.events.observer.observer_abc import Observer
from ethtx.events.observer.subject_abc import Subject


class EventSubject(Subject):
    _current_event_state: str = None
    _collection: str = EventCollection.COLLECTION.value
    _observers: List[Observer] = []

    @property
    def current_event_state(self) -> str:
        return self._current_event_state

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self, observer: Observer) -> None:
        for observer in self._observers:
            observer.update(self)

    def get_transaction_hash(self):
        pass

    def insert_event(self):
        pass

    def update_event(self):
        pass
