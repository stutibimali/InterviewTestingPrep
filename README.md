# FastAPI Debug Lab

A small, local-only FastAPI project for practicing request validation, route debugging, and runtime failure diagnosis. It uses only in-memory request data: there is no Azure resource, datastore, authentication, or external service.

## Codespace-like setup

From the project directory in a terminal:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -e ".[test]"
```

Select `.venv\\Scripts\\python.exe` as the VS Code Python interpreter. The checked-in `.vscode/settings.json` points Python tooling at that interpreter.

## Run the API

```powershell
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` for Swagger UI or `http://127.0.0.1:8000/redoc` for ReDoc.

Useful requests:

```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
Invoke-RestMethod -Method Post http://127.0.0.1:8000/calculate -ContentType 'application/json' -Body '{"first":6,"second":7,"operation":"multiply"}'
```

## Debug exercises

### Validation error

Request `http://127.0.0.1:8000/debug/validation-error?value=99`. FastAPI returns HTTP 422 because `value` must be an integer from 1 through 10. Set a breakpoint in `validation_error_scenario` and compare valid input (`value=5`) with invalid input. The invalid request fails during request validation, before the handler body runs.

### Runtime error

Request `http://127.0.0.1:8000/debug/runtime-error?trigger=true`. The route intentionally raises `RuntimeError` and returns HTTP 500. Set a breakpoint on the `raise` statement, inspect `trigger`, and step through the safe default request without the query parameter.

### Calculation path

POST `{"first": 8, "second": 2, "operation": "divide"}` to `/calculate`. Set a breakpoint in `app/calculator.py` and inspect each branch. Division by zero is intentionally left as a normal runtime failure for debugger practice.

## Tests

```powershell
.\.venv\Scripts\python.exe -m pytest
```

The suite covers healthy responses, successful calculation, Pydantic validation, the explicit validation scenario, the intentional runtime failure, and the safe runtime-scenario default.

## VS Code workflow

- `FastAPI: debug server` in `.vscode/launch.json` starts Uvicorn under `debugpy`.
- `Pytest: debug suite` runs the tests with breakpoints enabled.
- The `FastAPI: run` task starts the reload server.
- The `Tests: pytest` task runs the test suite.

Recommended sequence: start `FastAPI: debug server`, set a breakpoint in `app/main.py` or `app/calculator.py`, then exercise a route from Swagger UI. Use `Pytest: debug suite` to inspect assertions and error responses.

## Layout

```text
app/
  calculator.py  # deterministic calculation logic
  main.py        # FastAPI app and routes
  models.py      # Pydantic request and response models
tests/
  test_api.py    # focused API tests
.vscode/
  launch.json
  settings.json
  tasks.json
```
