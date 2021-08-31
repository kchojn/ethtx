import time
from typing import List, Set

from pydantic import BaseModel

from ethtx.events.observer.const import EventCollection
from ethtx.events.observer.observer_abc import Observer
from ethtx.events.observer.subject_abc import Subject


class EventSubject(Subject):
    _event_state: Set[BaseModel] = {}
    _current_event_state: str = None

    _collection: str = EventCollection.COLLECTION.value
    _observers: List[Observer] = []

    @property
    def event_state(self) -> Set[BaseModel]:
        return self._event_state

    @property
    def current_event_state(self) -> str:
        return self._current_event_state

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def notify_start(self, starts: time.time = time.time()) -> None:
        for observer in self._observers:
            observer.update(self, starts=starts)

    def notify_end(self, ends: time.time = time.time()) -> None:
        for observer in self._observers:
            observer.update(self, ends=ends)

    def get_transaction_hash(self):
        pass

    def insert_event(self):
        pass

    def update_event(self):
        pass
