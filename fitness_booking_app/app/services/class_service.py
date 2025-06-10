from zoneinfo import ZoneInfo
from datetime import datetime
from app.models.models import FitnessClass
from sqlalchemy.orm import Session
from typing import List


from app.logger import logger

def get_classes(db: Session, client_timezone="Asia/Kolkata"):
    logger.info(f"Fetching classes with timezone: {client_timezone}")
    tz = ZoneInfo(client_timezone)
    classes = db.query(FitnessClass).all()
    for cls in classes:
        cls.datetime = cls.datetime.astimezone(tz)
    logger.info(f"Returning {len(classes)} classes")
    return classes
