# 📦 Order API – Django REST Framework

This is a modular and scalable backend API for order and customer management built using **Django REST Framework (DRF)**. It includes full CRUD functionality, authentication, and clean separation of concerns via serializers, views, and models.

---

## 🧩 Project Structure

---

## 🛠️ Tech Stack

- **Backend:** Python, Django, Django REST Framework
- **Database:** SQLite (can be upgraded to PostgreSQL/MySQL)
- **Authentication:** Token-based (DRF Auth)

---

## 📁 Project Structure
order_api/
├── api/
│ ├── init.py
│ ├── admin.py # Admin interface setup
│ ├── apps.py # App config
│ ├── auth.py # Custom auth logic
│ ├── models.py # Database models
│ ├── serializers.py # DRF serializers
│ ├── tests.py # Unit tests
│ ├── urls.py # API URL routing
│ ├── views.py # API views/controllers
│ └── migrations/ # DB migrations
├── manage.py # Entry point
└── requirements.txt # Dependencies

---


---

## 🚀 Features

- 🔐 Token-based authentication (`auth.py`)
- 📦 CRUD operations for order-related data
- 🔄 RESTful architecture using `views.py`, `serializers.py`, and `models.py`
- 🔧 Admin panel for internal data management
- ✅ Easily extendable structure for additional apps or features

---

## 🛠️ Tech Stack

- **Framework:** Django, Django REST Framework
- **Language:** Python 3.x
- **Database:** SQLite (default), easily extendable to PostgreSQL/MySQL
- **Auth:** DRF token auth (via custom `auth.py`)

---

## ⚙️ Setup Instructions

```bash
# Clone the repository
git clone https://github.com/GautamSuthar8239/django_api.git
cd django_api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Migrate the database
python manage.py migrate

# Run the development server
python manage.py runserver

🧑‍💻 Developed By
Gautam Suthar
MCA Student | Backend & Full-Stack Developer
📍 Ahmedabad, India

---

Let me know if you want me to generate a **Postman collection**, **API docs**, or integrate it with your **Flutter frontend**!

