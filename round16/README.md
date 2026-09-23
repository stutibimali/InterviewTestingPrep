# Round 16 debugging practice

This independent round focuses on falsey values, configuration parsing,
sliding-window boundaries, pairwise arithmetic, and header-based API access.

Run it with:

```powershell
.\.venv\Scripts\python.exe -m pytest round16 -q
```

## Problem areas

- Distinguish missing values from valid falsey values such as zero and empty text.
- Trim configuration values and discard empty entries.
- Include the final valid sliding window.
- Preserve negative pairwise differences.
- Read a role from a request header and reject unsupported roles.