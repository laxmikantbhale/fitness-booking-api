from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List

from app.db import SessionLocal
from app.schemas.class_schema import ClassCreate, ClassOut
from app.services import class_service

router = APIRouter(tags=["Classes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.get("/classes", response_model=List[ClassOut])
def list_classes(
    timezone: str = Query(
        default="Asia/Kolkata",
        description=(
            "Timezone to display class times in.\n\n"
            "Recommended values:\n"
            "- UTC\n"
            "- Asia/Kolkata\n"
            "- America/New_York\n"
            "- America/Los_Angeles\n"
            "- Europe/London\n"
            "- Europe/Paris\n"
            "- Asia/Tokyo\n"
            "- Australia/Sydney"
        ),
    ),
    db: Session = Depends(get_db),
):
    """
    List all upcoming fitness classes, adjusting times to the requested timezone.
    """
    return class_service.get_classes(db, client_timezone=timezone)
