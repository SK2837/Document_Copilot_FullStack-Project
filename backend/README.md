# Backend

FastAPI service for Document Copilot.

## Setup

```bash
# Install dependencies
uv sync

# Install the package in editable mode (required for imports to work)
uv pip install -e .
```

Copy `.env.example` to `.env` and fill in your credentials before running.

## Run

```bash
# Development (auto-reload on file changes)
uv run uvicorn app.main:app --reload

# Or directly
uv run python app/main.py
```

Server runs at `http://127.0.0.1:8000`. Health check: `GET /health`

## Database migrations

```bash
# Apply all pending migrations
uv run alembic upgrade head

# Create a new migration (after editing SQLAlchemy models)
uv run alembic revision --autogenerate -m "describe your change"

# Rollback one step
uv run alembic downgrade -1
```

## Tests & lint

```bash
# Run tests
uv run pytest

# Lint + format check
uv run ruff check .
uv run ruff format --check .
```
