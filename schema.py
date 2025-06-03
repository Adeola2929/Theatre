from pydantic import BaseModel
from typing import Optional,List
from datetime import datetime


class SeatBase(BaseModel):
    RowNo : int
    SeatNo : int

class SeatCreate(SeatBase):
    pass

class SeatUpdate(BaseModel):
    RowNo : Optional[int]
    SeatNo : Optional[int]

class Seat(SeatBase):
    class Config:
        orm_mode = True

class TicketBase(BaseModel):
    Seat_RowNo : [int]
    Seat_SeatNo : [int]
    ShowTime_DateAndTime: datetime
    ShowTime_Play_PlayId : int
    Customer_CustomerId : int
    TicketNo: str

class TicketCreate(TicketBase):
    pass

class TicketUpdate(BaseModel):
    TicketNo : Optional[str]

class Ticket(TicketBase):
    class Config:
        orm_mode = True