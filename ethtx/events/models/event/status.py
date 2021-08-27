from sqlalchemy import Column, Integer, String

from ethtx.events.db.base_class import Base


class Status(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
