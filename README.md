# MatrixSols TopUp Project

A Django-based web application for managing game top-up orders and providing analytics for administrators. Includes REST API endpoints for top-up order creation and an analytics dashboard for insights.

## Features
- **Top-Up Order API**: Create top-up orders via REST API.
- **Analytics Dashboard**: View top 5 purchased products, daily revenue, and failed payments.
- **Admin Panel**: Manage products and orders with Django Admin.

## Tech Stack
- Python 3
- Django 4+
- Django REST Framework

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd matrixsols_topup_project
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   *(Create requirements.txt if missing: `django`, `djangorestframework`)*

4. **Configure environment variables**
   - Copy `.env.example` to `.env` and fill in required settings (if used)

5. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## API Endpoints
- `POST /api/topup/` — Create a new top-up order
- `GET /dashboard/` — View analytics dashboard (admin only)

## Folder Structure
```
matrixsols_topup_project/
├── topup/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── topup/dashboard.html
│   └── ...
├── matrixsols_topup_project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── manage.py
└── README.md
```

## Notes
- `__pycache__/`, `.env`, and `venv/` are git-ignored.
- Only staff/admin users can access the analytics dashboard.

## Contribution
PRs are welcome! Please open an issue first to discuss changes.

## License
[MIT](LICENSE) (add a LICENSE file if needed)
