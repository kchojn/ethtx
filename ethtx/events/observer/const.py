from enum import Enum


class EventState(str, Enum):
    TRANSACTION = "global"
    ABI = "abi"
    SEMANTICS = "semantics"


class EventCollection(str, Enum):
    COLLECTION = "events"
