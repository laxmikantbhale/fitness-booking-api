# 🏋️‍♂️ Fitness Studio Booking API

A simple API built using **FastAPI** and **SQLite** for booking fitness classes like Yoga, Zumba, and HIIT.
This project demonstrates clean architecture, timezone handling, and core backend skills.

---

## 📌 Features

* View upcoming fitness classes with timezone support
* Book a spot for a class (only one booking per user per class)
* View all bookings for a given email
* Handles overbooking and duplicate booking attempts
* Logging and input validation included

---

## 🚀 Tech Stack

* Python 3.10+
* FastAPI
* SQLite (in-memory or file-based)
* SQLAlchemy
* Pydantic
* Logging

---

## 🔧 Setup Instructions

### 1. Clone the repository or extract the zip

```bash
git clone <your-repo-url>
cd fitness_booking_app
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Seed initial data

```bash
python -m app.seed
```

### 5. Run the FastAPI app

```bash
uvicorn app.main:app --reload
```

---

## 🧲 API Endpoints

You can test all APIs using **Swagger UI** at:
📍 `http://127.0.0.1:8000/docs`

---

### 1. GET `/classes`

**Description**: Get all upcoming classes in your desired timezone.

**Query Parameters**:

* `timezone` (optional, default: `Asia/Kolkata`)

**Sample**:

```bash
curl -X GET "http://127.0.0.1:8000/classes?timezone=Europe/London"
```

---

### 2. POST `/book`

**Description**: Book a class by providing your name, email, and class ID.

**Sample**:

```bash
curl -X POST "http://127.0.0.1:8000/book" -H "Content-Type: application/json" -d '{
  "client_name": "Laxmikant",
  "client_email": "laxmikant@example.com",
  "class_id": 1
}'
```

---

### 3. GET `/bookings`

**Description**: Get all bookings made by a specific email.

**Query Parameters**:

* `client_email` (required)

**Sample**:

```bash
curl -X GET "http://127.0.0.1:8000/bookings?client_email=john@example.com"
```

---

## 📂 Project Structure

```
app/
├── main.py               # FastAPI app entry point
├── db.py                 # Database connection and init
├── seed.py               # Script to seed initial data
├── logger.py             # Logger setup
├── models/
│   └── models.py         # SQLAlchemy models
├── schemas/
│   ├── class_schema.py
│   └── booking_schema.py
├── services/
│   ├── class_service.py
│   └── booking_service.py
├── routers/
│   ├── classes.py
│   └── bookings.py
```

---

## ✅ Requirements Covered

* [x] GET /classes
* [x] POST /book (with duplicate booking restriction)
* [x] GET /bookings
* [x] SQLite in-memory DB
* [x] Timezone conversion
* [x] Logging
* [x] Input validation
* [x] Seed data with `python -m app.seed`
* [x] Swagger UI for testing

---

## 🎥 Loom Video

👉 *\[https://www.loom.com/share/02ba549ed17249c9a1c64d4adf4ffd99?sid=f3841fbf-e3c8-44ee-954c-871456837e0a]*
