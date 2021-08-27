from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from ethtx.events.db.base_class import Base


class Semantic(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    value = Column(String, nullable=False)

    transaction_id = Column(Integer, ForeignKey("transaction.id"))
    transaction = relationship("Transaction", backref="semantic")
