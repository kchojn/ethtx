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
import logging
from abc import ABCMeta, abstractmethod
from copy import deepcopy

log = logging.getLogger(__name__)


class LifoABC(ABCMeta("ABC", (object,), {"__slots__": ()})):
    """
    LIFO ABC implementation.
    """

    def __init__(self, max_size=0):
        self._lifo = None
        self._max_size = max_size
        self._full_len = 0

    def __call__(self, *args):
        self.push(*args)

    def __len__(self):
        return len(self.unpack())

    def __iadd__(self, other):
        full_len = self.full_len

        for data in other.unpack():
            self.push(data)

        self._full_len = full_len + other.full_len

        return self

    def __add__(self, other):
        lifo = deepcopy(self)
        full_len = lifo.full_len

        for data in other.unpack():
            lifo.push(data)

        lifo._full_len = full_len + other.full_len

        return lifo

    def __str__(self):
        return "%s(full_len='%s', len='%s', max_size='%s', elements=%s)" % (
            self.__class__.__name__,
            self.full_len,
            self.__len__(),
            self._max_size,
            self.unpack()[-10:],
        )

    def __repr__(self):
        return self.__str__()

    @property
    def full_len(self):
        """ Get number of added items (ignored max size) """
        return self._full_len

    @property
    def max_size(self):
        """ Max size """
        return self._max_size

    @max_size.setter
    def max_size(self, value):
        """ Change lifo max size. Inherit previous values. """
        data = list(self._lifo)
        self.__init__(value)
        self._inherit(data)

    @abstractmethod
    def push(self, data):
        """ Push single data or tuple/list to stack."""
        ...

    @abstractmethod
    def pop(self):
        """ Pop a single data """
        ...

    @abstractmethod
    def unpack(self):
        """ Unpack lifo """
        ...

    def _inherit(self, data):
        """ Inherit reinitialized lifo properties. """
        self._lifo.extend(data)
        self._full_len += len(data)
