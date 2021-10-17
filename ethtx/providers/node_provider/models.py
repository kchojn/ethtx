from __future__ import annotations

from typing import Any, List

from pydantic import BaseModel, Extra


class Event(BaseModel):
    type: str
    data: str
    topic0: str
    topic1: str
    topic2: str
    topic3: str


class CallStart(BaseModel):
    type: str
    id: str
    call_type: str
    gas: int
    to: str
    value: str
    data: str
    code_address: str
    event: Any
    call_end: Any
    sub_calls: list = []

    class Config:
        extra = Extra.allow


class CallEnd(BaseModel):
    type: str
    gas_used: int
    gas_refund: int
    return_value: str
    exception_error: str
    exception_error_type: str
    revert_reason: str
    success: bool
    memory_word_count: str


class TransactionStart(BaseModel):
    type: str
    no: int
    hash: str
    from_address: str
    to_address: str
    gas_limit: int
    gas_price: str


class TransactionEnd(BaseModel):
    type: str
    gas_used: int
    gas_refund: int
    created_address: str
    return_value: str
    exception_error: str
    exception_error_type: str
    revert_reason: str
    success: bool
    memory_word_count: str


class Transaction(BaseModel):
    metadata: Any = None
    root_call: Any = None
    events: List[Event] = None


tx_start_kwargs = dict(
    type="", no="", hash="", from_address="", to_address="", gas_limit="", gas_price=""
)

tx_end_kwargs = dict(
    type="",
    gas_used=None,
    gas_refund=None,
    created_address="",
    return_value="",
    exception_error="",
    exception_error_type="",
    revert_reason="",
    success=False,
    memory_word_count="",
)

call_start_kwargs = dict(
    type="", id="", call_type="", gas=0, to="", value="", data="", code_address=""
)

call_end_kwargs = dict(
    type="",
    gas_used=None,
    gas_refund=None,
    return_value="",
    exception_error="",
    exception_error_type="",
    revert_reason="",
    success=False,
    memory_word_count="",
)

event_kwargs = dict(type="", data="", topic0="", topic1="", topic2="", topic3="")
