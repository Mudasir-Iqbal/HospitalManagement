
# 🏥 Hospital Management System (HMS)

An enterprise-grade, production-ready Backend API built using **FastAPI** and **SQLAlchemy ORM**, featuring robust data validation, structured CRUD layers, and automated database migrations.

---

## 🚀 Tech Stack & Core Libraries

![Python](https://img.shields.io/badge/python-3.10+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg?style=for-the-badge&logo=fastapi&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red.svg?style=for-the-badge=logoColor=white)
![Alembic](https://img.shields.io/badge/Alembic-Migrations-orange.svg?style=for-the-badge)

---

## 🏗️ Clean Architecture & Folder Structure

Project ko professional software engineering principles ke mutabiq layer-by-layer structure kiya gaya hai taake scaling aur debugging aasan ho:

```text
HospitalManagement/
│
├── alembic/                  # Database Migration Versions & Scripts
├── app/
│   ├── crud/                 # Data Access Layer (Asli Database Queries)
│   │   ├── doctor.py
│   │   ├── patient.py
│   │   └── staff.py
│   │
│   ├── models/               # SQLAlchemy Models (Database Tables Schema)
│   │   ├── doctor.py
│   │   ├── patient.py
│   │   └── staff.py
│   │
│   ├── schemas/              # Pydantic Schemas (Data Validation Layers)
│   │   ├── doctor.py
│   │   ├── patient.py
│   │   └── staff.py
│   │
│   ├── routes/               # API Endpoints / Counters Manager
│   │   ├── doctor.py
│   │   ├── patient.py
│   │   └── staff.py
│   │
│   ├── database.py           # Database Connection Pooling & Session Engine
│   └── main.py               # Fast API Gateway & Application Entry Point
│
├── .gitignore
├── alembic.ini               # Alembic Migration Configuration
└── requirements.txt          # Project Dependencies

```

---

## 📊 Database Relational Schema

Project mein Tables ko **Relational Database Model** ke mutabiq design kiya gaya hai:

```
  +-------------------+             +-------------------+
  |      DOCTORS      |             |     PATIENTS      |
  +-------------------+             +-------------------+
  | id (PK)           | <---------\ | id (PK)           |
  | name              |            \| doctor_id (FK)    |
  | specialization    |             | name              |
  | email (Unique)    |             | age               |
  | phone             |             | gender            |
  | salary            |             | disease           |
  +-------------------+             | admission_date    |
                                    +-------------------+

  +-------------------+
  |       STAFF       |
  +-------------------+
  | id (PK)           |
  | name              |
  | role              |
  | shift             |
  | salary            |
  +-------------------+

```

### Key Engineering Features:

* **Foreign Key Constraints:** `Patients` table safely link hai `Doctors` table ke sath. Farzi Doctor ID par data validation request block ho jati hai.
* **On Delete Cascade:** Database integrity ko maintain karne ke liye advanced cascade behaviors configuration shamil hai.
* **Alembic Version Control:** Live production database par bina data loss kiye columns ko track aur migrate karne ki mukammal salahiyat.

---

## 🛠️ Installation & Setup Guide

Is project ko apne local system par run karne ke liye niche diye gaye steps ko follow karein:

### 1. Clone the Repository

```bash
git clone https://github.com/Mudasir-Iqbal/HospitalManagement.git
cd HospitalManagement

```

### 2. Virtual Environment Setup

```bash
python -m venv vhm
# Environment ko active karein:
# Windows:
vhm\Scripts\activate
# Mac/Linux:
source vhm/bin/activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Database Setup (`alembic.ini`)

Apne local MySQL server par `hospital_db` naam ka database create karein aur `alembic.ini` mein apni connection string update karein:

```ini
sqlalchemy.url = mysql+pymysql://USERNAME:PASSWORD@localhost:3306/hospital_db

```

### 5. Run Database Migrations

Database tables ko automatically apply karne ke liye Alembic migration chalaein:

```bash
alembic upgrade head

```

### 6. Start the Server

```bash
uvicorn app.main:app --reload

```

Server start hote ہی setup check karne ke liye is URL par jaaein:
🔗 **Interactive Swagger UI API Docs:** `http://127.0.0.1:8000/docs`

---

## 🎯 API Endpoints Documentation

### 🩺 Doctors Management

* `POST /doctor/` - Register a new doctor (with validation)
* `GET /doctor/` - Fetch list of all registered doctors
* `GET /doctor/{doctor_id}` - Retrieve details of a specific doctor
* `PUT /doctor/{doctor_id}` - Update doctor details dynamically
* `DELETE /doctor/{doctor_id}` - Remove a doctor from the system

### 🛌 Patients Management

* `POST /patient/` - Admit a new patient (Validates `doctor_id` before entry)
* `GET /patient/` - List all admitted patients
* `GET /patient/by-doctor/{doctor_id}` - Advanced analysis to get patients assigned to a specific doctor
* `DELETE /patient/{patient_id}` - Discharge patient from hospital

### 💼 Staff Management

* `POST /staff/` - Add a new hospital staff member
* `GET /staff/` - View all active staff members

---

💡 *Developed with precision and clean engineering practices.*

