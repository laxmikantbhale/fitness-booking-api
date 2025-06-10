from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class ClassCreate(BaseModel):
    title: str
    datetime: datetime  # naive or timezone-aware
    timezone: Optional[str] = "Asia/Kolkata"

class ClassOut(BaseModel):
    id: int
    title: str
    datetime: datetime  # will be converted to requested timezone
    instructor: str
    total_slots: int
    booked_slots: int

    class Config:
        orm_mode = True
