from ethtx.events.models.base import Base


class SemanticModel(Base):
    event_name: str = "decoded_semantics"
