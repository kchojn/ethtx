from ethtx.events.models.base import Base


class ABIModel(Base):
    event_name: str = "abi_decoding"
