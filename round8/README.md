# Round 8 debugging practice

This round is independent from the previous practice folders and contains new
functions, endpoints, and failure modes.

Run it with:

```powershell
.\.venv\Scripts\python.exe -m pytest round8 -q
```

## Problem areas

- Clamp values against both the lower and upper bound.
- Return a useful result for an empty mean calculation.
- Keep the last record when indexing duplicate keys.
- Preserve first-seen order while removing duplicates.
- Return HTTP 400 when path and body identifiers disagree.
- Use an appropriate status for a protected delete operation.

Debug one test at a time: reproduce the behavior, inspect the inputs and return
value, explain the root cause, then make the smallest correction.