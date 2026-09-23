# Round 10 debugging practice

This round is independent from all earlier practice folders and focuses on
input-shape handling, retry policy, arithmetic, merging, and query validation.

Run it with:

```powershell
.\.venv\Scripts\python.exe -m pytest round10 -q
```

## Problem areas

- Treat a single string as one tag rather than an iterable of characters.
- Parse negative range endpoints without splitting on the wrong delimiter.
- Retry server failures but not client errors such as rate limiting.
- Start exponential backoff at the configured base value.
- Add overlapping counters while preserving non-overlapping keys.
- Enforce a minimum search-query length through FastAPI validation.

Reproduce a failure, inspect the exact input shape and boundary, explain the
root cause, then rerun the smallest test after each fix.