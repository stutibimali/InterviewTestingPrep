# Round 13 debugging practice

This independent round focuses on CSV parsing, input normalization, ranking,
percentile boundaries, and FastAPI response contracts.

Run it with:

```powershell
.\.venv\Scripts\python.exe -m pytest round13 -q
```

## Problem areas

- Respect quoted commas in CSV rows.
- Strip header whitespace before converting it to snake case.
- Select highest-scoring items for a top-k result.
- Avoid an out-of-range percentile index at fraction `1.0`.
- Return a structured health response.
- Preserve an explicit `201 Created` endpoint status.