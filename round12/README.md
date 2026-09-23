# Round 12 debugging practice

This is an independent practice round with new path, date, ordering, and API
response-status cases.

Run it with:

```powershell
.\.venv\Scripts\python.exe -m pytest round12 -q
```

## Problem areas

- Strip parent directories from user-controlled filenames.
- Join URL fragments without duplicate slashes.
- Compare expiry timestamps using a consistent timezone.
- Sort events by their priority field.
- Return `201 Created` after accepting an upload.
- Enforce non-negative upload sizes through FastAPI validation.