from datetime import datetime, timedelta
from app.db import SessionLocal, engine, Base
from app.models.models import FitnessClass

def seed_classes():
    session = SessionLocal()
    try:
        # Optional: Clear existing data (be careful in production)
        session.query(FitnessClass).delete()
        session.commit()

        classes = [
            FitnessClass(
                title="Yoga",
                datetime=datetime.now() + timedelta(days=1),
                instructor="Sahil",
                total_slots=20,
                booked_slots=0
            ),
            FitnessClass(
                title="Zumba",
                datetime=datetime.now() + timedelta(days=2),
                instructor="Govind",
                total_slots=15,
                booked_slots=0
            ),
            FitnessClass(
                title="HIIT",
                datetime=datetime.now() + timedelta(days=3),
                instructor="Jaydeep",
                total_slots=10,
                booked_slots=0
            ),
        ]

        session.add_all(classes)
        session.commit()
        print("Seed data inserted!")
    except Exception as e:
        session.rollback()
        print(f"Error seeding data: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    # Ensure all tables exist before seeding
    Base.metadata.create_all(bind=engine)
    seed_classes()
