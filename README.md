# LeftOver – Django Backend

This is the backend for **LeftOver**, a food delivery web application.

## 🚀 Features

- ✅ Custom user model with roles (`customer`, `restaurant`)
- ✅ Restaurant profile management
- ✅ Menu system (sections & items)
- ✅ Django REST Framework API
- ✅ Ready for microservice architecture & cloud deployment

## 📂 Project Structure

leftover/
├── accounts/ # Custom users, customer & restaurant profiles
├── backend/ # Django project settings
├── menu/ # Menu sections and items
├── manage.py
├── requirements.txt
└── .gitignore

#bash

## 📦 Installation

```bash
git clone https://github.com/mrskibby/leftover-backend.git
cd leftover-backend
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

🔜 Next Goals
API filtering & permissions

Order management app

Authentication & role-based access

Frontend integration (React)

👤 Author
Nazmus Sakib – @mrskibby
