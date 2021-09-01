import datetime
from threading import Lock
from typing import List, Set, Union, Literal

from pydantic import BaseModel

from ethtx.events.observer.const import EventCollection
from ethtx.events.observer.observer_abc import Observer
from ethtx.events.observer.subject_abc import Subject


class EventSubject(Subject):
    _current_event_state: str = None

    _collection: str = EventCollection.COLLECTION.value
    _observers: List[Observer] = []

    def __init__(self):
        self.lock = Lock()

    @property
    def current_event_state(self) -> str:
        return self._current_event_state

    def attach(self, observer: Union[Observer, List[Observer]]) -> None:
        if isinstance(observer, list):
            self._observers.extend(observer)
        else:
            self._observers.append(observer)

    def detach(self, observer: Union[Observer, List[Observer]]) -> None:
        if isinstance(observer, list):
            for o in observer:
                self._observers.remove(o)
        else:
            self._observers.remove(observer)

    def notify(self, *args, **kwargs) -> None:
        for observer in self._observers:
            observer.update(self, *args, **kwargs)

    def notify_start(self, starts: datetime.datetime = datetime.datetime.now()) -> None:
        for observer in self._observers:
            observer.update(self, starts=starts)

    def notify_end(self, ends: datetime.datetime = datetime.datetime.now()) -> None:
        for observer in self._observers:
            observer.update(self, ends=ends)

    def get_transaction_hash(self):
        pass

    def insert_event(self):
        pass

    def update_event(self):
        pass

    def set_event_state(self, state: Literal["abi", "semantics", "global"]) -> None:
        self._current_event_state = state
