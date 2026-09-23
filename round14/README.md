# Round 14 debugging practice

This independent round focuses on floating-point totals, character validation,
date parsing, ordered deduplication, and FastAPI query validation.

Run it with:

```powershell
.\.venv\Scripts\python.exe -m pytest round14 -q
```

## Problem areas

- Round the final taxed total rather than relying on intermediate float behavior.
- Validate every slug character, not merely one allowed character.
- Parse ISO dates in year-month-day order.
- Preserve first-seen order during deduplication.
- Let FastAPI coerce query strings while enforcing page boundaries.