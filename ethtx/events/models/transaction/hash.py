from sqlalchemy import Column, Integer, String

from ethtx.events.db.base_class import Base


class Hash(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    value = Column(String, index=True, nullable=False)
