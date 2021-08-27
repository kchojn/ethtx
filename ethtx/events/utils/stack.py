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

from collections import deque

from .lifo_abc import LifoABC


class Stack(LifoABC):
    """
    Stack implementation.
    Set maximum size of stack.
    Append elements, if max_size is full, then append and delete form the beginning.
    """

    def __init__(self, max_size=None):
        super().__init__(max_size=max_size)
        self._lifo = deque(maxlen=max_size)

    def push(self, data):
        """ Push single data or tuple/list to stack."""
        if data:
            self._lifo.append(data)
            self._full_len += 1

    def pop(self):
        """ Pop single data """
        data = None

        if self.unpack():
            data = self._lifo.pop()
            self._full_len -= 1

        return data

    def unpack(self):
        """ Unpack deque object. """
        return list(self._lifo)
