# Round 3 debugging practice

This is a separate set of FastAPI and Python debugging exercises. It intentionally
uses different names, domains, and failure modes from `practice/` and `problem2/`.

Run only this round while practicing:

```powershell
.\.venv\Scripts\python.exe -m pytest round3 -q
```

The tests describe the contract. The challenge files contain the defects; explain
the failure and fix the smallest root cause.

## Suggested 45-minute exercise

1. Start with one failing test and reproduce it without changing code.
2. Trace the input, the intermediate value, and the returned value.
3. Explain why the implementation disagrees with the test contract.
4. Make one focused fix and rerun only that test.

## New problem areas

- Parse textual feature flags without treating every non-empty string as true.
- Group multiple shipment records under the same region.
- Calculate a fractional mean instead of truncating it.
- Preserve an integer field in a FastAPI response contract.
- Handle naive and timezone-aware timestamps consistently.
- Avoid state leaking between calls through a mutable default argument.

The exercises are intentionally not solutions. During an assessment, use the
failure output and official documentation rather than an AI assistant.