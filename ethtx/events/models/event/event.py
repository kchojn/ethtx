from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from ethtx.events.db.base_class import Base


class Event(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    object_key = Column(Integer, nullable=False, index=True)
    object_verb = Column(String)
    object_name = Column(String, index=True)

    event_priority = Column(Integer, ForeignKey("priority.id"))
    priority = relationship("Priority", backref="event")

    event_time = Column(DateTime)

    event_status = Column(Integer, ForeignKey("status.id"))
    status = relationship("Status", backref="event")

    event_comment = Column(String)
