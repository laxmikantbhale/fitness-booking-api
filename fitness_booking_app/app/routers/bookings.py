from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.schemas.booking_schema import BookingCreate, BookingResponse
from app.services import booking_service
from app.db import SessionLocal

router = APIRouter(tags=["Bookings"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/book", response_model=BookingResponse, status_code=201)
def book_class(booking: BookingCreate, db: Session = Depends(get_db)):
    """
    Book a spot in a fitness class.
    """
    return booking_service.create_booking(db, booking)

@router.get("/bookings", response_model=List[BookingResponse])
def get_bookings(client_email: str = Query(..., description="Client's email address"), db: Session = Depends(get_db)):
    """
    Retrieve all bookings made by a specific client email.
    """
    bookings = booking_service.get_bookings_by_email(db, client_email)
    if not bookings:
        raise HTTPException(status_code=404, detail="No bookings found for this email")
    return bookings
