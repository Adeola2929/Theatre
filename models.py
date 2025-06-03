from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Seat(Base):
    __tablename__ = "seats"

    id = Column(Integer, primary_key=True, index=True)
    row_number = Column(Integer)
    seat_number = Column(Integer)

    tickets = relationship("Ticket", back_populates="seat")
    prices = relationship("Price", back_populates="seat")


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    seat_id = Column(Integer, ForeignKey("seats.id"))
    show_time_id = Column(Integer, ForeignKey("show_times.id"))
    customer_id = Column(Integer, ForeignKey("customers.id"))

    seat = relationship("Seat", back_populates="tickets")
    show_time = relationship("ShowTime", back_populates="tickets")
    customer = relationship("Customer", back_populates="tickets")