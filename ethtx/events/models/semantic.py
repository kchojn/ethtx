from pydantic import validator

from ethtx.events.models.base import Base


class SemanticModel(Base):
    event_name: str = None

    @validator("event_name", pre=True, always=True)
    def validate_event_name(cls, v: str) -> str:
        return "semantics_decoding" if not v else v
