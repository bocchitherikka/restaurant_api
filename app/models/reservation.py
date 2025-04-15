from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from app.services.db import Base


class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String)
    table_id = Column(Integer, ForeignKey("tables.id", ondelete="CASCADE"))
    reservation_time = Column(DateTime)
    duration_minutes = Column(Integer)
