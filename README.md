# LeftOver – Django Backend

This is the secure backend API for **LeftOver**, a food rescue and delivery platform. Built with Django and Django REST Framework, it provides robust authentication, restaurant management, and menu APIs with cloud-ready architecture.


## 🚀 Features

- ✅ **Secure JWT Authentication** (access & refresh via `HttpOnly` cookies)
- ✅ **Logout with token blacklisting**
- ✅ **Rate-limited login** to prevent brute-force attacks
- ✅ **Custom user model** with roles (`customer`, `restaurant`)
- ✅ **Restaurant profile** management
- ✅ **Menu system** (sections & items)
- ✅ **Modular, microservice-ready** architecture
- ✅ **GitHub Actions CI** for automated testing

## 📂 Project Structure

leftover/
├── accounts/ # Custom users, customer & restaurant profiles
├── backend/ # Django project settings
├── menu/ # Menu sections and items
├── users/ # Authentication logic (login, logout, refresh)
├── manage.py
├── requirements.txt
├── .env # Secret keys and config (not committed)
├── .gitignore
└── .github/workflows # GitHub Actions CI

#bash

## 🛠️ Installation & Setup

```bash
git clone https://github.com/mrskibby/leftover-backend.git
cd leftover-backend

# Setup virtual environment
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create your .env file
copy .env.example .env  # or manually add SECRET_KEY, DEBUG, etc.

# Run migrations and server
python manage.py migrate
python manage.py runserver


🔐 Security Features
Features:
JWT access + refresh cookies	✅
Token rotation & blacklisting	✅
CSRF/XSS-safe cookies	✅
Login rate limiting	✅
HTTPS-ready configuration	✅


🧪 CI/CD
This project includes:

✅ Automated test runs on every push via GitHub Actions

Easily extensible to deployment workflows (Heroku, Render, etc.)


🔜 Next Goals
 API filtering, search, and pagination

 Role-based permissions

 Stripe payment integration

 Admin dashboard for food tracking

 Frontend (React/Next.js) integration

👤 Author
Nazmus Sakib – @mrskibby
