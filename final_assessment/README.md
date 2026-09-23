# Final integrated FastAPI debugging assessment

This folder combines the main interview topics from the previous practice
rounds into one fresh, 45-minute debugging exercise. The implementation is
intentionally broken. The tests are the behavioral contract.

Run only the final assessment:

```powershell
.\.venv\Scripts\python.exe -m pytest final_assessment -q
```

## Topic coverage

- Environment variables and JSON configuration
- Core Python calculations and floating-point rounding
- Ordered collections and duplicate removal
- Input parsing and type conversion
- Pydantic field constraints
- Pydantic cross-field validation
- FastAPI query, path, and body parameters
- HTTP `201`, `404`, and `422` behavior
- Response-model validation and response types
- Search boundaries and pagination-style limits
- Error messages and traceback-driven debugging

## 45-minute format

1. Spend five minutes running the suite and grouping failures by topic.
2. Spend thirty minutes fixing one failure at a time.
3. After each fix, run the narrowest test and explain the root cause aloud.
4. Spend the final ten minutes checking edge cases and summarizing tradeoffs.

## Interview checklist

- Read the traceback before changing code.
- Reproduce the smallest failing input.
- Identify whether the problem is parsing, validation, business logic, or HTTP behavior.
- Make the smallest root-cause fix.
- Confirm the endpoint status, response shape, and response types.
- Mention what additional test you would add in production.