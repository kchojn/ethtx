from typing import List, Any

from pydantic import BaseModel

from ethtx.events.models.abi import ABIModel
from ethtx.events.models.base import Base
from ethtx.events.models.semantic import SemanticModel
from ethtx.events.utils.helpers import utc_timestamp_to_id


class Meta(BaseModel):
    address_semantics: List[Any] = []
    signature_semantics: List[Any] = []


class TransactionModel(Base):
    id: int = utc_timestamp_to_id()
    hash: str
    abi: ABIModel
    semantic: SemanticModel
    meta: Meta


class FullTransactionModel(BaseModel):
    id: str
    transaction: TransactionModel
