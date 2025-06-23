# Tech Survey Frontend

A beautiful, interactive survey form for collecting technology-related feedback.

## Features

- 🎨 Modern, responsive design with glassmorphism effects
- 🔊 Interactive sound effects (toggleable)
- ✅ Real-time form validation
- 📱 Mobile-friendly interface
- 🚀 Vercel deployment ready
- 🔗 Backend API integration

## Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd tech-survey-frontend
   ```

2. **Open in browser**
   Simply open `index.html` in your browser or use a local server:
   ```bash
   # Using Python
   python -m http.server 8000
   
   # Using Node.js (http-server)
   npx http-server
   
   # Using Live Server (VS Code extension)
   Right-click index.html -> "Open with Live Server"
   ```

## Vercel Deployment

1. **Install Vercel CLI** (optional)
   ```bash
   npm install -g vercel
   ```

2. **Deploy to Vercel**
   
   **Option A: Using Vercel CLI**
   ```bash
   vercel
   ```
   
   **Option B: Using GitHub Integration**
   - Push your code to GitHub
   - Connect repository to Vercel
   - Automatic deployments on every push

3. **Configure Environment**
   After deployment, update the API configuration in `index.html`:
   ```javascript
   const API_CONFIG = {
     BASE_URL: 'https://your-railway-backend.railway.app',
     ENDPOINTS: {
       SURVEY: '/api/survey'
     }
   };
   ```

## Configuration

### Backend URL Setup

Update the `API_CONFIG` object in `index.html`:

```javascript
const API_CONFIG = {
  BASE_URL: 'YOUR_RAILWAY_BACKEND_URL', // Replace with your Railway backend URL
  ENDPOINTS: {
    SURVEY: '/api/survey'
  }
};
```

### CORS Configuration

Make sure your backend allows requests from your Vercel domain:

```javascript
const corsOptions = {
  origin: [
    'https://your-vercel-app.vercel.app', // Your Vercel URL
    'http://localhost:3000',
    // ... other allowed origins
  ]
};
```

## Features

### Interactive Sound Effects
- Toggle sound on/off with the speaker button
- Soft click sounds for form interactions
- Success melody on form submission
- Gentle focus sounds for input fields

### Form Validation
- Real-time validation for all fields
- Email format validation
- Required field checking
- Custom error messages

### Responsive Design
- Mobile-first approach
- Glassmorphism effects
- Smooth animations and transitions
- Beautiful gradient backgrounds

## File Structure

```
├── index.html          # Main HTML file with embedded CSS and JS
├── vercel.json         # Vercel deployment configuration
└── README.md          # This file
```

## Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers

## License

MIT License
