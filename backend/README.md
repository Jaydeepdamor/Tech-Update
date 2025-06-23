# Tech Survey Backend

Django REST API backend for the Technology Survey application.

## Setup for Local Development

### Prerequisites
- Python 3.11+ 
- pip

### Quick Start

#### Windows
```bash
# Run the setup script
start_dev.bat
```

#### Unix/Linux/MacOS
```bash
# Make script executable
chmod +x start_dev.sh

# Run the setup script
./start_dev.sh
```

#### Manual Setup
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Unix/Linux/MacOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

## Railway Deployment

1. Push your code to a GitHub repository
2. Connect Railway to your GitHub repository
3. Set the following environment variables in Railway:
   - `SECRET_KEY`: Your Django secret key
   - `DEBUG`: False
   - `DATABASE_URL`: (Railway will provide this automatically for PostgreSQL)
   - `ALLOWED_HOSTS`: your-app-name.railway.app
   - `CORS_ALLOWED_ORIGINS`: https://your-vercel-app.vercel.app

## API Endpoints

- `POST /api/survey/submit/` - Submit survey response
- `GET /api/survey/stats/` - Get survey statistics
- `GET /api/health/` - Health check endpoint
- `GET /admin/` - Django admin interface

## Environment Variables

Create a `.env` file based on `.env.example`:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

## Project Structure

```
backend/
├── manage.py
├── requirements.txt
├── techsurvey/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── survey/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py
    ├── urls.py
    ├── views.py
    └── migrations/
```
