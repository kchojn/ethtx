from ethtx.events.models.base import Base


class ABIModel(Base):
    event_name: str = "decoded_abi"
