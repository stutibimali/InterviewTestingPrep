# Round 7 debugging practice

This round is independent from the earlier practice folders. It uses different
functions and failure modes and is intended for focused interview drills.

Run it with:

```powershell
.\.venv\Scripts\python.exe -m pytest round7 -q
```

## Problem areas

- Normalize phone numbers by removing all formatting separators.
- Keep the final characters visible when redacting a token.
- Initialize grouped counters at zero rather than one.
- Append a running total after adding the current value.
- Convert a ratio into a percentage instead of returning a fraction.
- Respect an exclusive end boundary in a window helper.
- Use an HTTP 403 response for an invalid API key.
- Enforce a Pydantic severity range.

Reproduce one failing test, state the expected and actual values aloud, fix the
smallest root cause, and rerun that test before moving on.