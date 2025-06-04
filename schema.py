from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class SeatBase(BaseModel):
    RowNo: int
    SeatNo: int

class SeatCreate(SeatBase):
    pass

class SeatUpdate(BaseModel):
    RowNo: Optional[int]
    SeatNo: Optional[int]

class Seat(SeatBase):
    id: int

    class Config:
        from_attributes = True


class Customer(BaseModel):
    id: int
    name: Optional[str]

    class Config:
        from_attributes = True

class ShowTime(BaseModel):
    id: int
    date_and_time: datetime

    class Config:
        from_attributes = True


class TicketBase(BaseModel):
    TicketNo: str
    ShowTime_Play_PlayId: int  # Still keep for creation
    ShowTime_DateAndTime: datetime
    Customer_CustomerId: int
    Seat_RowNo: List[int]
    Seat_SeatNo: List[int]

class TicketCreate(TicketBase):
    pass

class TicketUpdate(BaseModel):
    TicketNo: Optional[str]

# Response model with relationships
class Ticket(TicketBase):
    id: int
    seat: Optional[Seat]             # 💡 Nested relationship
    customer: Optional[Customer]
    show_time: Optional[ShowTime]

    class Config:
        from_attributes = True
