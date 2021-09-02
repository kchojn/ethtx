from typing import List, Any, Optional

from pydantic import validator, BaseModel

from ethtx.events.models.abi import ABIModel
from ethtx.events.models.base import Base
from ethtx.events.models.semantic import SemanticModel
from ethtx.events.utils.helpers import utc_timestamp_to_id


class Meta(BaseModel):
    address_semantics: Optional[List[Any]] = []
    signature_semantics: Optional[List[Any]] = []


class TransactionModel(Base):
    id: int = None
    event_name: str = None
    abi: Optional[ABIModel] = None
    semantic: Optional[SemanticModel] = None
    meta: Optional[Meta] = None

    @validator("id", pre=True, always=True)
    def validate_id(cls, v: int) -> int:
        return utc_timestamp_to_id() if not v else v

    @validator("event_name", pre=True, always=True)
    def validate_event_name(cls, v: str) -> str:
        return "transaction_decoding" if not v else v


class FullTransactionModel(BaseModel):
    hash: Optional[str] = None
    transaction: Optional[TransactionModel] = None
