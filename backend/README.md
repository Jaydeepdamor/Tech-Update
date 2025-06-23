# Tech Survey Backend API

A RESTful API backend for the Technology Survey form, designed to be deployed on Railway.

## Features

- 🚀 RESTful API with Express.js
- 🔒 Security middleware (Helmet, CORS, Rate Limiting)
- ✅ Input validation with express-validator
- 📊 Survey response storage and statistics
- 🎯 Admin endpoints for data retrieval
- 🐳 Railway deployment ready

## Local Development

1. **Install Dependencies**
   ```bash
   npm install
   ```

2. **Environment Setup**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Start Development Server**
   ```bash
   npm run dev
   ```

4. **Start Production Server**
   ```bash
   npm start
   ```

## API Endpoints

### Public Endpoints

- `GET /` - API status
- `GET /health` - Health check
- `POST /api/survey` - Submit survey response

### Admin Endpoints

- `GET /api/survey/responses` - Get all survey responses (paginated)
- `GET /api/survey/stats` - Get survey statistics

## API Usage

### Submit Survey Response

```javascript
POST /api/survey
Content-Type: application/json

{
  "timestamp": "2025-06-23T12:00:00.000Z",
  "question1": "Yes",
  "question2": "No",
  "question3": ["Option 1", "Option 2"],
  "email": "user@gmail.com",
  "otherSpecification": "Additional details..."
}
```

### Response Format

```javascript
{
  "success": true,
  "message": "Survey response submitted successfully",
  "data": {
    "id": "1624456800000",
    "timestamp": "2025-06-23T12:00:00.000Z"
  }
}
```

## Railway Deployment

1. **Connect Repository**
   - Connect your GitHub repository to Railway
   - Railway will automatically detect the Node.js project

2. **Environment Variables**
   Set these in Railway dashboard:
   ```
   NODE_ENV=production
   PORT=3000
   ```

3. **Deploy**
   - Railway will automatically deploy on every push to main branch
   - Your API will be available at: `https://your-app-name.railway.app`

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `NODE_ENV` | Environment mode | `development` |
| `PORT` | Server port | `3000` |
| `RATE_LIMIT_WINDOW_MS` | Rate limit window | `900000` (15 min) |
| `RATE_LIMIT_MAX_REQUESTS` | Max requests per window | `100` |

## Security Features

- **Helmet**: Security headers
- **CORS**: Cross-origin request handling
- **Rate Limiting**: Prevent abuse
- **Input Validation**: Sanitize and validate input
- **Error Handling**: Secure error responses

## Data Storage

Currently uses in-memory storage. For production, consider:
- MongoDB with Mongoose
- PostgreSQL with Sequelize
- SQLite for simple deployments

## Frontend Integration

Update your frontend configuration:

```javascript
const API_CONFIG = {
  BASE_URL: 'https://your-app-name.railway.app',
  ENDPOINTS: {
    SURVEY: '/api/survey'
  }
};
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.
