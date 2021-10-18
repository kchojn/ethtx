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
from pprint import pprint
from typing import Generator, List

import requests

from ethtx.providers.node_provider.models import (
    tx_start_kwargs,
    Call,
    TransactionMetadata,
    tx_end_kwargs,
    Event,
    event_kwargs,
    call_end_kwargs,
    call_start_kwargs,
    Transaction,
)
from ethtx.providers.node_provider.utils import match_dict, update_model


class NodeProvider:
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self.http = requests.Session()

        self._block = None
        self._transaction = None
        self._full_transaction = None
        self._root_call = None
        self._events = []

        self._content: List[str] = []

    def get_block(self, block_number: int):
        ...

    def get_transaction(self, tx_hash: str):
        if not self._transaction:
            stream = self._content if self._content else self._stream(tx_hash)
            for line in stream:

                if line[0] != "txEnd" and "tx" in line[0]:
                    tx = TransactionMetadata(**match_dict(tx_start_kwargs, line[2:]))

                if line[0] == "txEnd":
                    self._transaction = update_model(
                        tx, match_dict(tx_end_kwargs, line[1:])
                    )
                    break

        return self._transaction

    def get_full_transaction(self, tx_hash: str):
        if not self._full_transaction:
            self.get_transaction(tx_hash)
            self.get_calls(tx_hash)
            self.get_events(tx_hash)

            self._full_transaction = Transaction(
                metadata=self._transaction,
                root_call=self._root_call,
                events=self._events,
            )

        return self._full_transaction

    def get_calls(self, tx_hash: str):
        calls = []
        if not self._root_call:
            stream = self._content if self._content else self._stream(tx_hash)
            for line in stream:
                if line[0] == "call" and not line[1]:
                    root_call = Call(**match_dict(call_start_kwargs, line[1:]))
                    print(111111, root_call)
                    calls.append(root_call)

                if line[0] == "call" and line[1]:
                    sub_call = Call(**match_dict(call_start_kwargs, line[1:]))
                    calls.append(sub_call)

                if line[0] == "callEnd":
                    for c in reversed(calls):
                        if c.success is None:
                            data = match_dict(call_end_kwargs, line[1:])
                            update_model(c, data)
                            break

            for call in calls:
                self._make_call_tree(call, root_call)

            self._root_call = root_call

        return self._root_call

    def get_events(self, tx_hash: str):
        if not self._events:
            stream = self._content if self._content else self._stream(tx_hash)
            for line in stream:
                if line[0] == "event":
                    event = Event(**match_dict(event_kwargs, line[1:]))
                    self._events.append(event)

        return self._events

    def _build_url(self, tx_hash: str):
        return f"{self.connection_string}/{tx_hash}"

    def _stream(self, tx_hash: str) -> Generator[List[str], None, None]:
        to_return = False

        with self.http.get(
            self._build_url(tx_hash), headers=None, stream=True
        ) as response:
            for line in response.iter_lines():

                if line and tx_hash in line.decode():
                    to_return = True

                if line and to_return:
                    return_line = line.rstrip().decode().split(",")
                    self._content.append(return_line)
                    yield return_line

    def _make_call_tree(self, sub_call, call=None):
        if len(sub_call.id) == 1:
            call.sub_calls.append(sub_call)
            return

        for i in call.sub_calls:
            if (
                i.id in sub_call.id
                and i.id.count("_") + 1 == sub_call.id.count("_")
                and i.id == sub_call.id.rsplit("_", 1)[0]
            ):
                i.sub_calls.append(sub_call)
                return
            elif (
                len(sub_call.id) == len(i.id) and i.id == sub_call.id.rsplit("_", 1)[0]
            ):
                call.sub_calls.append(sub_call)
                return
            else:
                self._make_call_tree(sub_call, i)
