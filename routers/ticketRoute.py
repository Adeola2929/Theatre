from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import schema
from services import ticket_service
from typing import List

ticket_router = APIRouter(prefix="/tickets", tags=["Tickets"])

@ticket_router.post("/", response_model=schema.Ticket)
def create_ticket(ticket_data: schema.TicketCreate, db: Session = Depends(get_db)):
    return ticket_service.create_ticket(db, ticket_data)

@ticket_router.get("/", response_model=List[schema.Ticket])
def get_all_tickets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return ticket_service.get_all_tickets(db, skip=skip, limit=limit)

@ticket_router.get("/{ticket_id}", response_model=schema.Ticket)
def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = ticket_service.get_ticket_by_id(db, ticket_id)
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

@ticket_router.put("/{ticket_id}", response_model=schema.Ticket)
def update_ticket(ticket_id: int, ticket_data: schema.TicketUpdate, db: Session = Depends(get_db)):
    ticket = ticket_service.update_ticket(db, ticket_id, ticket_data)
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

@ticket_router.delete("/{ticket_id}")
def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):
    result = ticket_service.delete_ticket(db, ticket_id)
    if not result:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return {"message": "Ticket deleted successfully"}
