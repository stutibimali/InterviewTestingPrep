# Round 9 debugging practice

This round is independent from all previous practice folders and focuses on
conversion, lookup, partitioning, and REST behavior.

Run it with:

```powershell
.\.venv\Scripts\python.exe -m pytest round9 -q
```

## Problem areas

- Parse common true and false strings instead of recognizing one spelling.
- Format the remainder of a duration as seconds within the current minute.
- Return a default when a nested path is missing at any level.
- Preserve order while partitioning even and odd values.
- Return `202 Accepted` when a job is queued.
- Return `404 Not Found` for a missing job.

Practice by reproducing each failure, identifying the smallest incorrect
assumption, and rerunning the focused test after the fix.