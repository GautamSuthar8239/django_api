# 🔧 Car Service Management API – Django REST Framework

This is the backend API for a full-stack **Car Service Management System**, built using **Django** and **Django REST Framework**. It provides endpoints for managing service bookings, customers, inventory, billing, and more.

---

## 🚀 Features

- 🔐 Token-based user authentication
- 🧾 CRUD APIs for customers, services, mechanics, and inventory
- 🗓️ Booking and service tracking
- 💳 Billing and invoice generation endpoints
- 📦 Inventory and parts management
- 📊 Admin-friendly and scalable design

---

## 🛠️ Tech Stack

- **Backend:** Python, Django, Django REST Framework
- **Database:** SQLite (can be upgraded to PostgreSQL/MySQL)
- **Authentication:** Token-based (DRF Auth)

---

## 📁 Project Structure
/django_api
│
├── car_service/ # Main Django app for business logic
├── car_service_api/ # Project settings, URLs, and WSGI config
├── db.sqlite3 # SQLite Database
├── manage.py # Entry point
└── requirements.txt # Dependencies



---

## ⚙️ Setup Instructions

```bash
# Clone the repo
git clone https://github.com/GautamSuthar8239/django_api.git
cd django_api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Run development server
python manage.py runserver


POST /api/token/
{
  "username": "your_username",
  "password": "your_password"
}
🧑‍💻 Developed By
Gautam Suthar
MCA Student | Backend & Full-Stack Developer
📍 Ahmedabad, India

---

Let me know if you want me to generate a **Postman collection**, **API docs**, or integrate it with your **Flutter frontend**!

