import datetime
from threading import Lock
from typing import List, Union, Literal

from ethtx.events.observer.const import EventCollection, EVENT_TYPE
from ethtx.events.observer.observer_abc import Observer
from ethtx.events.observer.subject_abc import Subject


class EventSubject(Subject):
    _current_event_type: str = None

    _collection: str = EventCollection.COLLECTION.value
    _observers: List[Observer]

    def __init__(self):
        self._observers = []
        self.lock = Lock()

    @property
    def current_event_type(self) -> str:
        return self._current_event_type

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

    def notify_start(self) -> None:
        for observer in self._observers:
            observer.update(self, starts=datetime.datetime.now())

    def notify_end(self) -> None:
        for observer in self._observers:
            observer.update(self, ends=datetime.datetime.now())
        self.clear_event_state()

    def set_event_state(self, state: EVENT_TYPE) -> None:
        self._current_event_type = state

    def clear_event_state(self) -> None:
        self._current_event_type = ""

    def get_transaction_hash(self):
        pass

    def insert_event(self):
        pass

    def update_event(self):
        pass
