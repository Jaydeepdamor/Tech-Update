# Tech Survey Application

A modern, full-stack survey application to understand technology learning challenges. Built with Django REST Framework backend and vanilla HTML/CSS/JavaScript frontend.

## 🚀 Live Demo

- **Frontend**: `https://YOUR_VERCEL_APP.vercel.app` (Deploy to Vercel)
- **Backend API**: `https://YOUR_RAILWAY_APP.railway.app` (Deploy to Railway)

## 📋 Project Overview

This survey application helps understand the challenges technology professionals face when trying to stay updated with cutting-edge advancements. It features:

- Modern glassmorphism UI design
- Real-time form validation
- Interactive sound effects
- Mobile-responsive design
- RESTful API backend
- Admin dashboard for response management

## 🛠 Tech Stack

### Frontend
- **HTML5/CSS3/JavaScript** - Pure vanilla implementation
- **Web Audio API** - For interactive sound effects
- **Responsive Design** - Mobile-first approach
- **Vercel** - Deployment platform

### Backend
- **Django 4.2** - Web framework
- **Django REST Framework** - API development
- **PostgreSQL** - Production database (Railway)
- **SQLite** - Development database
- **Railway** - Deployment platform

## 🏗 Project Structure

```
Tech Update/
├── frontend/
│   ├── index.html          # Main survey form
│   ├── vercel.json         # Vercel deployment config
│   ├── package.json        # Package info
│   └── README.md
│
├── backend/
│   ├── manage.py           # Django management
│   ├── requirements.txt    # Python dependencies
│   ├── Procfile           # Railway deployment
│   ├── railway.toml       # Railway config
│   ├── runtime.txt        # Python version
│   ├── start_dev.bat      # Windows development
│   ├── start_dev.sh       # Unix development
│   ├── .env.example       # Environment template
│   ├── .gitignore         # Git ignore rules
│   ├── README.md
│   │
│   ├── techsurvey/        # Main Django project
│   │   ├── __init__.py
│   │   ├── settings.py    # Django settings
│   │   ├── urls.py        # URL routing
│   │   ├── wsgi.py        # WSGI application
│   │   └── asgi.py        # ASGI application
│   │
│   └── survey/            # Survey Django app
│       ├── __init__.py
│       ├── admin.py       # Admin interface
│       ├── apps.py        # App configuration
│       ├── models.py      # Database models
│       ├── serializers.py # API serializers
│       ├── urls.py        # App URLs
│       ├── views.py       # API views
│       └── migrations/    # Database migrations
│
└── README.md              # This file
```

## 🚀 Deployment Guide

### Backend Deployment (Railway)

1. **Prepare Repository**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/tech-survey.git
   git push -u origin main
   ```

2. **Deploy to Railway**
   - Go to [Railway](https://railway.app)
   - Connect your GitHub repository
   - Select the `backend` folder as root
   - Add PostgreSQL database service
   - Set environment variables (see backend/.env.example)

3. **Environment Variables** (Set in Railway Dashboard):
   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=False
   ALLOWED_HOSTS=your-app-name.railway.app,localhost,127.0.0.1
   CORS_ALLOWED_ORIGINS=https://your-vercel-app.vercel.app,http://localhost:3000
   ```

### Frontend Deployment (Vercel)

1. **Update API Configuration**
   - Edit `frontend/index.html`
   - Replace `YOUR_RAILWAY_APP_NAME` with your Railway app name

2. **Deploy to Vercel**
   - Go to [Vercel](https://vercel.com)
   - Connect your GitHub repository
   - Select the `frontend` folder as root
   - Deploy automatically

## 🔧 Local Development

### Backend Setup

#### Windows
```bash
cd backend
start_dev.bat
```

#### Unix/Linux/MacOS
```bash
cd backend
chmod +x start_dev.sh
./start_dev.sh
```

### Frontend Setup

```bash
cd frontend
# Open index.html in browser or serve with:
python -m http.server 3000
```

## 📊 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/survey/submit/` | Submit survey response |
| GET | `/api/survey/stats/` | Get survey statistics |
| GET | `/api/health/` | Health check |
| GET | `/admin/` | Django admin interface |

## 🔒 Security Features

- CORS protection
- CSRF protection
- Input validation and sanitization
- XSS protection headers
- SQL injection prevention (Django ORM)
- Secure headers for production

## 📝 Environment Variables Guide

### Backend (.env)

```env
# Required
SECRET_KEY=your-django-secret-key
DEBUG=False
DATABASE_URL=postgresql://user:pass@host:port/dbname

# Optional
ALLOWED_HOSTS=your-domain.railway.app,localhost
CORS_ALLOWED_ORIGINS=https://your-frontend.vercel.app
```

### Frontend (JavaScript)

Update the API configuration in `index.html`:

```javascript
const API_CONFIG = {
    BASE_URL: 'https://YOUR_RAILWAY_APP_NAME.railway.app',
    ENDPOINTS: {
        SURVEY: '/api/survey/submit/'
    }
};
```

## 🐛 Troubleshooting

### Common Issues

1. **CORS Errors**
   - Ensure `CORS_ALLOWED_ORIGINS` includes your frontend URL
   - Check that the frontend API_CONFIG points to correct backend URL

2. **Database Issues**
   - Railway automatically provides PostgreSQL DATABASE_URL
   - For local development, SQLite is used automatically

3. **Static Files**
   - WhiteNoise is configured for serving static files in production
   - Collect static files: `python manage.py collectstatic`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 📞 Support

For support, please open an issue in the GitHub repository.

---

**Remember to replace all placeholder URLs with your actual deployment URLs!**
