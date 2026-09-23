# Round 15 debugging practice

This independent round focuses on complete-string validation, required fields,
cache isolation, input immutability, and FastAPI response models.

Run it with:

```powershell
.\.venv\Scripts\python.exe -m pytest round15 -q
```

## Problem areas

- Match the entire identifier rather than accepting a valid prefix.
- Distinguish missing fields from fields present with falsey values.
- Include namespace in a cache key.
- Return a new list instead of mutating a caller-owned list.
- Let FastAPI response models remove internal response fields.