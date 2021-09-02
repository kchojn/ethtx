from enum import Enum
from typing import Literal


class EventType(str, Enum):
    GLOBAL = "global"
    TRANSACTION = "transaction"
    ABI = "abi"
    SEMANTICS = "semantics"


class EventCollection(str, Enum):
    COLLECTION = "events"


EVENT_TYPE = Literal["abi", "global", "transaction", "semantics"]
