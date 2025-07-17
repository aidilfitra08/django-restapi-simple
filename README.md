# 🧩 django-restapi-simple

A minimal Django REST API with JWT authentication built using Django REST Framework.  
This project is suitable for backend services that need to serve data securely to mobile or frontend applications (e.g., React, Next.js, Vue).

---

## 🚀 Features

- Django 4+
- Django REST Framework (DRF)
- JWT authentication with `djangorestframework-simplejwt`
- Token refresh & verify support
- API protected with `IsAuthenticated`
- JSON-only token endpoints (no browsable UI)
- Ready for use with Postman, Insomnia, or frontend clients

---

## 📁 Project Structure

```
django-restapi-simple/
├── api/                    # Django app with views, models, serializers
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── myapi/                  # Django project settings and config
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── venv/                   # Virtual environment
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/django-restapi-simple.git
cd django-restapi-simple
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### 6. Run the server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)

---

## 🔐 JWT Authentication

### 🔸 Obtain Token

```http
POST /api/token/
Content-Type: application/json

{
  "username": "yourusername",
  "password": "yourpassword"
}
```

**Response:**

```json
{
  "access": "access_token_here",
  "refresh": "refresh_token_here"
}
```

### 🔄 Refresh Token

```http
POST /api/token/refresh/

{
  "refresh": "your_refresh_token"
}
```

**Response:**

```json
{
  "access": "new_access_token"
}
```

### ✅ Verify Token

```http
POST /api/token/verify/

{
  "token": "your_token"
}
```

---

## 🔐 Accessing Protected Routes

To access endpoints like `/api/todos/`, include the token in the header:

```http
GET /api/todos/
Authorization: Bearer <your-access-token>
```

---

## 🧪 Development Tools

Install formatters and linters:

```bash
pip install black isort djlint
```

### Format Code

```bash
black .
isort .
```

### Format Django Templates

```bash
djlint templates/
```

---

## 📌 Notes

- JWT token expiration time and refresh config is set in `settings.py` via the `SIMPLE_JWT` dictionary.
- You can change token lifetimes, rotation, and blacklist settings there.
- Token views return JSON only (no HTML browsable API for security).

---

## 🧠 Useful Commands

```bash
# Run development server
python manage.py runserver

# Make and apply migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

---

## 📜 License

MIT License — feel free to use, modify, and share.

---

## 🙋‍♂️ Author

**Your Name**  
🔗 GitHub: [@aidilfitra08](https://github.com/aidilfitra08)
