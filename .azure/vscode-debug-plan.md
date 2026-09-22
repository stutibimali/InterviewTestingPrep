# Local VS Code Debugging Plan

**Status**: Implemented
**Created**: 2026-09-21
**Execution Mode**: manual

## Project Target

Configure local VS Code debugging for the `fastapi-debug-lab` Python project. The project is a local-only FastAPI ASGI service with no Azure resources, database, authentication, or external service dependencies.

## Runtime

- Use the project virtual environment at `${workspaceFolder}\\.venv\\Scripts\\python.exe`.
- Run the ASGI application as the `uvicorn` module with `app.main:app`.
- Use the existing reload-based run task for normal development.
- Keep `PYTHONUNBUFFERED=1` for predictable debugger and terminal output.
- Preserve the existing Python test discovery settings for the `tests` directory.

## Debug Configurations

1. **FastAPI: debug server**
   - Launch `uvicorn` through `debugpy` using `app.main:app --reload`.
   - Enable `justMyCode` so breakpoints in `app/` are prioritized.
   - Support breakpoints in `app/main.py`, `app/calculator.py`, and request-model validation boundaries.

2. **Pytest: debug suite**
   - Launch the `pytest` module against `tests` with quiet output.
   - Enable `justMyCode` so test and application breakpoints are inspectable.

## Tasks and Editor Settings

- Provide a `FastAPI: run` process task using the project interpreter and Uvicorn reload mode.
- Provide a `Tests: pytest` process task using the project interpreter.
- Set the project interpreter to `.venv\\Scripts\\python.exe`.
- Enable pytest discovery and disable unittest discovery.
- Add the workspace root to Python analysis paths.

## Validation Plan

- Run `python -m pytest` from the project virtual environment and confirm all existing tests pass.
- Start the debug server and verify `GET /health` returns the healthy service response.
- Verify `POST /calculate` reaches `app/calculator.py` and returns the expected multiplication result.
- Verify `GET /debug/validation-error?value=99` returns HTTP 422 before the route body executes.
- Verify `GET /debug/runtime-error?trigger=true` pauses on the intentional `RuntimeError` and returns HTTP 500 when continued.
- Verify `GET /debug/runtime-error` follows the safe default path with HTTP 200.
- Keep all validation local and confirm no Azure or persistent-service configuration is required.

## Artifacts

- `.vscode/launch.json`: debug server and pytest debug configurations.
- `.vscode/tasks.json`: run and test tasks.
- `.vscode/settings.json`: interpreter and test discovery settings.
