# 🐍 Django Stock Manager

Backend application built with **Python and Django** for managing products and stock movements in an organized and structured way.

This project focuses on applying backend fundamentals such as data modeling, business rules, and code organization using Django’s native tools.

---

## 📌 About the Project

Django Stock Manager is a backend system designed to control products and their stock movements. The application uses Django’s ORM to persist data and applies clear separation of responsibilities between models, views, and configurations.

The project is currently **in development** and serves as a practical backend exercise aligned with real-world scenarios such as inventory control and data consistency.

---

## ⚙️ Technologies Used

* Python
* Django
* Django ORM
* SQLite (default database)
* HTML (templates for basic views)

---

## 🧱 Project Structure

```text
config/          # Project configuration and settings
inventory/       # Main app for stock management
  ├── models.py  # Data models (products and stock movements)
  ├── views.py   # Application views
  ├── forms.py   # Django forms
  ├── admin.py   # Admin configuration
  └── templates/ # HTML templates
manage.py        # Django management script
```

---

## 🗄️ Main Features

* Product registration
* Stock movement control (entries and exits)
* Data persistence using Django ORM
* Admin interface for data management
* Basic HTML templates for interaction

---

## ▶️ How to Run the Project Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/Devv-ictor/django-stock-manager.git
   cd django-stock-manager
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:

   ```bash
   pip install django
   ```

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Access the application at:

   ```
   http://127.0.0.1:8000/
   ```

---

## 🚧 Project Status

🔧 **In development** — new features and improvements are being added as part of continuous learning and backend practice.

---

## 🎯 Learning Goals

* Strengthen backend development skills with Django
* Practice data modeling and business logic
* Improve code organization and maintainability
* Simulate real-world backend scenarios

---

## 👤 Author

**Victor Alexandre Silva**
Backend-focused developer working with Python and Django.

* GitHub: [https://github.com/Devv-ictor](https://github.com/Devv-ictor)
* LinkedIn: [https://linkedin.com/in/victor-alexandre-silva](https://linkedin.com/in/victor-alexandre-silva)
