from app.logger import logger
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.models import Booking, FitnessClass
from app.schemas.booking_schema import BookingCreate

def create_booking(db: Session, booking: BookingCreate):
    logger.info(f"Booking request received: {booking.client_name} for class_id {booking.class_id}")

    # Check if the class exists
    fitness_class = db.query(FitnessClass).filter(FitnessClass.id == booking.class_id).first()
    if not fitness_class:
        logger.error(f"Fitness class with id {booking.class_id} not found.")
        raise HTTPException(status_code=404, detail="Fitness class not found")

    # Check for duplicate booking
    existing_booking = db.query(Booking).filter(
        Booking.client_email == booking.client_email,
        Booking.class_id == booking.class_id
    ).first()

    if existing_booking:
        logger.warning(f"Duplicate booking attempt by {booking.client_email} for class_id {booking.class_id}")
        raise HTTPException(status_code=400, detail="You have already booked this class")

    # Check for available slots
    available_slots = fitness_class.total_slots - fitness_class.booked_slots
    if available_slots <= 0:
        logger.warning(f"No slots available for class_id {booking.class_id}. Booking rejected.")
        raise HTTPException(status_code=400, detail="No available slots")

    # Create booking
    db_booking = Booking(
        client_name=booking.client_name,
        client_email=booking.client_email,
        class_id=booking.class_id
    )
    fitness_class.booked_slots += 1
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    logger.info(f"Booking successful for {booking.client_name} in class_id {booking.class_id}")
    return db_booking

def get_bookings_by_email(db: Session, email: str):
    logger.info(f"Fetching bookings for email: {email}")
    return db.query(Booking).filter(Booking.client_email == email).all()
