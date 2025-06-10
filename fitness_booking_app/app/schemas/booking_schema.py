from pydantic import BaseModel, EmailStr, Field

class BookingBase(BaseModel):
    client_name: str = Field(..., example="John Doe")
    client_email: EmailStr
    class_id: int

class BookingCreate(BookingBase):
    pass

class BookingResponse(BookingBase):
    id: int

    class Config:
        orm_mode = True
