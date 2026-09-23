# Round 4 debugging practice

This round is independent from `practice/`, `problem2/`, and `round3/`. It uses
new problem names and failure modes. The implementation files are intentionally
broken; the tests define the expected behavior.

Run it with:

```powershell
.\.venv\Scripts\python.exe -m pytest round4 -q
```

## Problem areas

- A generator is consumed before rejected records are counted.
- A shallow copy changes nested data in the original record.
- Sorting uses the wrong direction for ranking.
- A set destroys the order of unique values.
- Environment JSON must be decoded into structured data.
- FastAPI query parameters should be supplied in the query string.
- Cross-field validation must reject a request larger than available stock.

Practice each failure by reproducing it, identifying the smallest root cause,
explaining your reasoning aloud, and running the narrowest test after the fix.