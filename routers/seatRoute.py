from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import schema
from services import seat_service
from typing import List

seat_router = APIRouter(prefix="/seats", tags=["Seats"])

@seat_router.post("/", response_model=schema.Seat)
def create_seat(seat_data: schema.SeatCreate, db: Session = Depends(get_db)):
    return seat_service.create_seat(db, seat_data)

@seat_router.get("/", response_model=List[schema.Seat])
def get_all_seats(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return seat_service.get_all_seats(db, skip=skip, limit=limit)

@seat_router.get("/{seat_id}", response_model=schema.Seat)
def get_seat(seat_id: int, db: Session = Depends(get_db)):
    seat = seat_service.get_seat_by_id(db, seat_id)
    if seat is None:
        raise HTTPException(status_code=404, detail="Seat not found")
    return seat

@seat_router.put("/{seat_id}", response_model=schema.Seat)
def update_seat(seat_id: int, seat_data: schema.SeatUpdate, db: Session = Depends(get_db)):
    seat = seat_service.update_seat(db, seat_id, seat_data)
    if seat is None:
        raise HTTPException(status_code=404, detail="Seat not found")
    return seat

@seat_router.delete("/{seat_id}")
def delete_seat(seat_id: int, db: Session = Depends(get_db)):
    result = seat_service.delete_seat(db, seat_id)
    if not result:
        raise HTTPException(status_code=404, detail="Seat not found")
    return {"message": "Seat deleted successfully"}
