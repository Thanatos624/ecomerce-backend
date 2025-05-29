# 🛒 E-Commerce Backend API

A powerful and minimal Django REST Framework backend for handling Users, Products, and Orders with JWT Authentication.

---

## 🚀 Quick Start

### 1. Clone & Setup Virtual Environment

```bash
git clone <your-repo-url>
cd ecommercebackend
python -m venv venv
venv\Scripts\activate         # Windows  
source venv/bin/activate     # macOS/Linux
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Django

Edit `settings.py`:

```python
STATIC_URL = '/static/'
```

### 4. Setup PostgreSQL

Make sure PostgreSQL is installed and configured, then in `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ecomdb',
        'USER': 'postgres',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## 🛠️ Run Migrations & Create Superuser

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

---

## ▶️ Run the Server

```bash
python manage.py runserver
```

---

## 🔐 Admin Panel

- URL: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- Login using your superuser credentials

👨‍🔧 Can't login?

```bash
python manage.py shell
```

```python
from users.models import CustomUser
user = CustomUser.objects.get(email="your_email")
user.is_staff = True
user.set_password("newpassword")
user.save()
```

---

## 🔑 JWT Authentication

### Get Token

```http
POST /api/token/
Content-Type: application/json

{
  "email": "your_email",
  "password": "your_password"
}
```

### Use Token in Header

```http
Authorization: Bearer <your_access_token>
```

---

## 📁 Project Structure

```
ecommercebackend/
├── users/
├── products/
├── orders/
├── ecommercebackend/
├── screenshots/
│   └── admin-permissions.png
├── manage.py
└── README.md
```

---

## 🖼️ Screenshot



![image](https://github.com/user-attachments/assets/124356e3-cafd-45b9-bce1-c033d01061a6)





