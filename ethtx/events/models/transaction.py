from typing import List, Any, Optional

from pydantic import BaseModel

from ethtx.events.models.abi import ABIModel
from ethtx.events.models.base import Base
from ethtx.events.models.semantic import SemanticModel
from ethtx.events.utils.helpers import utc_timestamp_to_id


class Meta(BaseModel):
    address_semantics: Optional[List[Any]] = []
    signature_semantics: Optional[List[Any]] = []


class TransactionModel(Base):
    _id: int = utc_timestamp_to_id()
    hash: Optional[str] = None
    abi: Optional[ABIModel] = None
    semantic: Optional[SemanticModel] = None
    meta: Optional[Meta] = None


class FullTransactionModel(BaseModel):
    _id: str
    transaction: TransactionModel
