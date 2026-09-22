# Integration Handoff

This project is intentionally local-only and has no frontend, datastore, authentication, or Azure resources. No live-data integration or migrations are required.

## Backend

- Folder: project root
- Run: `.venv\\Scripts\\python.exe -m uvicorn app.main:app --reload`
- Port: `8000`
- Build/validation: `.venv\\Scripts\\python.exe -m compileall -q app tests` and `.venv\\Scripts\\python.exe -m pytest`
- Health: `GET /health`

## Frontend

- None planned.

## API routes

- `GET /health`
- `POST /calculate`
- `GET /debug/validation-error?value=<integer 1..10>`
- `GET /debug/runtime-error?trigger=<boolean>`
- OpenAPI docs: `GET /docs`

## Database

- None. No migration tool, migration directory, connection environment variables, or seed data.

## Shared types

- None; Pydantic models live in `app/models.py`.

## Services

- Essential: FastAPI Debug Lab, local Python virtual environment, Uvicorn.
- Enhancement: none.
