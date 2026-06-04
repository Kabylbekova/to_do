# 📝 ToDo List — REST API

A RESTful backend for a task management application built with Django and Django REST Framework.

## 🚀 Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/Django_REST_Framework-ff1709?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

## ✨ Features

- Create, read, update and delete tasks (CRUD)
- RESTful API with JSON responses
- Django admin panel
- Clean project structure with separated app modules

## 📁 Project Structure

```
to_do/
├── API/              # Project configuration (settings, urls, wsgi)
├── blog/             # Main app (models, views, serializers, urls)
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
└── manage.py
```

## ⚙️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/Kabylbekova/to_do.git
cd to_do

# Install dependencies
pip install -r API/req.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

## 📬 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/tasks/` | Get all tasks |
| POST | `/api/tasks/` | Create a new task |
| PUT | `/api/tasks/{id}/` | Update a task |
| DELETE | `/api/tasks/{id}/` | Delete a task |

---
Made with ❤️ by [Burul Kabylbekova](https://github.com/Kabylbekova)

