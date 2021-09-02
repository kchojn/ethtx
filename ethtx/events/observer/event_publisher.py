import datetime
from threading import Lock
from typing import List, Union, Dict

from mongoengine import connect
from pydantic import BaseModel
from pymongo.database import Database

from ethtx.events.models.transaction import FullTransactionModel
from ethtx.events.observer.const import EventCollection, EVENT_TYPE, EVENT_STATE
from ethtx.events.observer.observer_abc import Observer
from ethtx.events.observer.subject_abc import Subject


class EventSubject(Subject):
    event: BaseModel = None

    _current_event_state: Dict[EVENT_TYPE, EVENT_STATE] = {}
    _collection: str = EventCollection.COLLECTION.value

    _observers: List[Observer]
    _emitted_events: Dict[EVENT_TYPE, BaseModel]

    def __init__(self):
        self.lock = Lock()
        self.db: Database = connect("ethtx", host="mongomock://localhost/ethtx").db
        self._events = self.db["events"]

        self._observers = []
        self._emitted_events = {}

    @property
    def current_event_state(self) -> Dict[EVENT_TYPE, EVENT_STATE]:
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

    def notify_start(self, event: EVENT_TYPE) -> None:
        self.set_event_state(event=event, state="start")
        for observer in self._observers:
            observer.update(self, starts=datetime.datetime.now())

    def notify_end(self, event: EVENT_TYPE) -> None:
        self.set_event_state(event=event, state="end")
        for observer in self._observers:
            observer.update(self, ends=datetime.datetime.now())

        self.clear_event_state()

    def set_event_state(self, event: EVENT_TYPE, state: EVENT_STATE) -> None:
        self._current_event_state = {event: state}

    def clear_event_state(self) -> None:
        self._current_event_state = {}

    def emit_event(self, event: Dict[EVENT_TYPE, BaseModel]) -> None:
        self._emitted_events.update(event)

    def group_transaction_events(self) -> None:
        self.event: FullTransactionModel = self._emitted_events.get("global")
        if self.event:
            self.event.transaction.append(self._emitted_events.get("transaction"))
            if self.event.transaction:
                self.event.transaction[0].abi = self._emitted_events.get("abi")
                self.event.transaction[0].semantics = self._emitted_events.get(
                    "semantics"
                )

    def get_transaction_event(self, hash: str):
        return self._events.find_one({"_id": hash})

    def insert_transaction_event(self):
        event_with_id = {
            "_id": self.event.hash,
            **self.event.dict(exclude_none=True, exclude={"hash"}),
        }
        return self._events.insert_one(event_with_id)

    def update_transaction_event(self):
        self._events.update_one(
            {"_id": self.event.hash},
            {
                "$push": {
                    "transaction": self.event.transaction[0].dict(exclude_none=True)
                }
            },
        )
