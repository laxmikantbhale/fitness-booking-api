from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base

class FitnessClass(Base):
    __tablename__ = "classes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    datetime = Column(DateTime, nullable=False)
    instructor = Column(String, nullable=False)
    total_slots = Column(Integer, nullable=False)
    booked_slots = Column(Integer, default=0)

    bookings = relationship("Booking", back_populates="fitness_class")

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String, nullable=False)
    client_email = Column(String, nullable=False)
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)

    fitness_class = relationship("FitnessClass", back_populates="bookings")