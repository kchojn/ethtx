from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship

from ethtx.events.db.base_class import Base


class Transaction(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    hash = Column(Integer, ForeignKey("hash.id"))
    hashes = relationship("Hash", backref="transaction")

    type = Column(Integer, ForeignKey("type.id"))
    types = relationship("Type", backref="transaction")

    starts = Column(DateTime, nullable=False)
    ends = Column(DateTime)
    duration = Column(Float)
