from enum import Enum


class EventState(str, Enum):
    transaction = "global"
    abi = "abi"
    semantics = "semantics"
