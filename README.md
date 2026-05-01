# disaster_flask_app

A modernized Flask application with app-factory pattern, environment-based config, structured logging, and an AI-powered `/ask` endpoint.

## Quick Start

```bash
cp .env.example .env
# Edit .env with your values
pip install -r requirements.txt
python run.py
```

## Docker

```bash
docker build -t disaster_flask_app .
docker run -p 8000:8000 --env-file .env disaster_flask_app
```

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `SECRET_KEY` | Yes | Flask secret key |
| `DATABASE_URL` | No | PostgreSQL URL (defaults to SQLite) |
| `FLASK_ENV` | No | `development` or `production` |
| `ANTHROPIC_API_KEY` | No | Enables `/ask` AI endpoint |
| `PORT` | No | Server port (default: 8000) |

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Hello world page |
| `/surnames/?Name=John+Doe` | GET | Parse surname from name |
| `/health` | GET | Health check with uptime |
| `/diag` | GET | Service diagnostics |
| `/ask` | POST | AI-powered Q&A (Claude) |

### `/ask` Example

```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is the capital of France?"}'
```

## Architecture

```
app/
├── __init__.py      # Application factory
├── config.py        # Env-based config (Dev/Prod)
├── models.py        # SQLAlchemy models
├── errors.py        # 404/500 error handlers
└── routes/
    ├── main.py      # Core routes
    ├── health.py    # Health & diagnostics
    └── ai.py        # Claude AI endpoint
```

## AI Innovation

Set `ANTHROPIC_API_KEY` to unlock the `/ask` endpoint — a natural language interface backed by Claude. Extend it to query your database, analyze logs, or answer domain-specific questions.
