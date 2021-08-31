from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra


class Base(BaseModel):
    starts: Optional[datetime] = None
    ends: Optional[datetime] = None

    exception: Optional[str] = None
    message: Optional[str] = None

    class Config:
        extra = Extra.allow
