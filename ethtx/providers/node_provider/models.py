from __future__ import annotations

from typing import List, Optional

from pydantic import Extra, BaseModel


class Event(BaseModel):
    data: str
    topic0: str
    topic1: str
    topic2: str
    topic3: str


class Call(BaseModel):
    id: str
    call_type: str
    gas: int
    to: str
    value: str
    data: str
    code_address: str
    gas_used: Optional[int]
    gas_refund: Optional[int]
    return_value: Optional[str]
    exception_error: Optional[str]
    exception_error_type: Optional[str]
    revert_reason: Optional[str]
    success: Optional[bool]
    memory_word_count: Optional[str]
    sub_calls: list = []

    class Config:
        extra = Extra.allow


class TransactionMetadata(BaseModel):
    hash: str
    from_address: str
    to_address: str
    gas_limit: int
    gas_price: str
    gas_used: Optional[int]
    gas_refund: Optional[int]
    created_address: Optional[str]
    return_value: Optional[str]
    exception_error: Optional[str]
    exception_error_type: Optional[str]
    revert_reason: Optional[str]
    success: Optional[bool]
    memory_word_count: Optional[str]


class Transaction(BaseModel):
    metadata: TransactionMetadata
    root_call: Call
    events: List[Event] = []


tx_start_kwargs = dict(
    hash="", from_address="", to_address="", gas_limit="", gas_price=""
)

tx_end_kwargs = dict(
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
    id="", call_type="", gas=0, to="", value="", data="", code_address=""
)

call_end_kwargs = dict(
    gas_used=None,
    gas_refund=None,
    return_value="",
    exception_error="",
    exception_error_type="",
    revert_reason="",
    success=None,
    memory_word_count="",
)

event_kwargs = dict(data="", topic0="", topic1="", topic2="", topic3="")
