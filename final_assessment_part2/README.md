# Final integrated assessment, Part 2

Part 2 is a second integrated 45-minute exercise. It focuses on nested request
models, aggregate validation, pagination, patch semantics, dependency checks,
and HTTP status behavior.

Run only Part 2:

```powershell
.\.venv\Scripts\python.exe -m pytest final_assessment_part2 -q
```

## Topics

- One-based pagination and slice boundaries
- Explicit falsey PATCH values
- Quantity and unit-price arithmetic
- Nested Pydantic models
- Cross-field aggregate validation
- FastAPI dependencies and request headers
- Admin authorization with `403 Forbidden`
- Creation with `201 Created`
- Missing resources with `404 Not Found`

Use the same interview routine: reproduce the failure, locate the controlling
function or route, explain the root cause, make one focused fix, and rerun the
narrowest test.