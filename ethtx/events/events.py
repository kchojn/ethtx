#  Copyright 2021 DAI Foundation
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at: http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
from typing import TypeVar, Dict

from ethtx.events.observer.const import EVENT_TYPE, EventType
from ethtx.events.observer.event_publisher import EventSubject
from ethtx.events.observer.event_subscribers import (
    GlobalEventObserver,
    ABIEventObserver,
    SemanticsEventObserver,
    TransactionEventObserver,
)

EVENT_STORE_TYPE = TypeVar("EVENT_STORE_TYPE", bound=Dict[str, EventSubject])


class EthTxEvents:
    _events: EVENT_STORE_TYPE

    def __init__(self):
        self._events = {}

    def record(self, event_type: EVENT_TYPE = None):
        def decorator(f):
            def wrapper(*args, **kwargs):
                if len(args) > 1:
                    tx_hash = [
                        h for h in args if isinstance(h, str) and h.startswith("0x")
                    ][0]
                else:
                    tx_hash = kwargs["transaction"].metadata.tx_hash

                if tx_hash not in self._events:
                    publisher = EventSubject()
                    subscribers = [
                        GlobalEventObserver(),
                        TransactionEventObserver(),
                        ABIEventObserver(),
                        SemanticsEventObserver(),
                    ]
                    publisher.attach(subscribers)
                    self._events[tx_hash] = publisher

                    self._events[tx_hash].set_event_state(event="global", state="start")
                    self._events[tx_hash].notify(hash=tx_hash)

                self._events[tx_hash].notify_start(event=event_type)

                try:
                    self._events[tx_hash].set_event_state(
                        event=event_type, state="processing"
                    )
                    func_o = f(*args, **kwargs)
                except Exception as e:
                    self._events[tx_hash].notify(exception=e)
                    raise e

                self._events[tx_hash].notify_end(event=event_type)

                if event_type == EventType.GLOBAL:
                    self._events[tx_hash].group_transaction_events()
                    del self._events[tx_hash]

                return func_o

            return wrapper

        return decorator

    def push(self, metric_name: str):
        def decorator(f):
            def wrapper(*args, **kwargs):
                func_o = f(*args, **kwargs)
                data = {metric_name: func_o}

                return func_o

            return wrapper

        return decorator


monitor = EthTxEvents()
