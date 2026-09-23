# Round 11 debugging practice

This independent round adds new shape, mapping, serialization, and FastAPI error
handling exercises.

Run it with:

```powershell
.\.venv\Scripts\python.exe -m pytest round11 -q
```

## Problem areas

- Compare sequence lengths for equality rather than only one ordering.
- Preserve falsey values such as zero during fallback lookup.
- Serialize dictionaries with deterministic key ordering.
- Return `404 Not Found` for missing resources.
- Keep a query parameter as a query parameter when testing a simple endpoint.