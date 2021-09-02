from ethtx.events.models.base import Base


class SemanticModel(Base):
    event_name: str = "semantics_decoding"
