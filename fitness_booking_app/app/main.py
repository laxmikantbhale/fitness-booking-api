from fastapi import FastAPI
from app.db import init_db
from app.routers import classes, bookings
from app.logger import logger

app = FastAPI(title="Fitness Studio Booking API")

app.include_router(classes.router)
app.include_router(bookings.router)

@app.on_event("startup")
def startup_event():
    init_db()
    logger.info("Database initialized and app startup complete")
