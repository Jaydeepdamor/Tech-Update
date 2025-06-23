# Tech Survey Frontend

A beautiful, modern survey form for technology professionals to understand their learning challenges.

## Features

- 🎨 Modern glassmorphism design
- 📱 Fully responsive
- 🔊 Interactive sound effects
- ✨ Smooth animations
- 🎯 Real-time validation
- 🌐 Ready for Vercel deployment

## Setup for Local Development

1. Open `index.html` in a web browser, or
2. Serve with a local server:

```bash
# Using Python
python -m http.server 3000

# Using Node.js (if you have it)
npx serve . -p 3000
```

## Vercel Deployment

1. Push your code to a GitHub repository
2. Connect Vercel to your GitHub repository
3. Deploy automatically

### Configuration

Before deployment, update the API configuration in `index.html`:

```javascript
const API_CONFIG = {
    BASE_URL: 'https://your-railway-app.railway.app', // Replace with your Railway backend URL
    ENDPOINTS: {
        SURVEY: '/api/survey/submit/'
    }
};
```

## File Structure

```
frontend/
├── index.html          # Main survey form
├── vercel.json         # Vercel deployment config
├── package.json        # NPM package info
└── README.md           # This file
```

## Browser Support

- Chrome/Edge 88+
- Firefox 85+
- Safari 14+

## API Integration

The frontend connects to a Django REST API backend with the following endpoint:

- `POST /api/survey/submit/` - Submit survey responses

## Customization

### Styling
All styles are embedded in the HTML file using CSS custom properties for easy theming.

### Sound Effects
Sound effects can be toggled on/off by users. They're generated using the Web Audio API.

### Validation
Real-time form validation provides immediate feedback to users.

## Security Features

- Input sanitization
- CORS headers
- XSS protection
- Content Security Policy ready
