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
from typing import Literal, TypeVar, Dict

from ethtx.events.observer.event_publisher import EventSubject
from ethtx.events.observer.event_subscribers import (
    GlobalEventObserver,
    ABIEventObserver,
    SemanticsEventObserver,
    TransactionEventObserver,
)

EventStoreType = TypeVar("EventStoreType", bound=Dict[str, EventSubject])


class EthTxEvents:
    _events: EventStoreType = {}

    def record(self, type: Literal["abi", "semantics", "global", "transaction"] = None):
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
                    self._events = {tx_hash: publisher}

                    self._events[tx_hash].set_event_state("global")
                    self._events[tx_hash].notify(hash=tx_hash)

                if type == "transaction":
                    self._events[tx_hash].set_event_state("transaction")
                elif type == "abi":
                    self._events[tx_hash].set_event_state("abi")
                elif type == "semantics":
                    self._events[tx_hash].set_event_state("semantics")

                self._events[tx_hash].notify_start()
                func_o = f(*args, **kwargs)
                self._events[tx_hash].notify_end()

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
