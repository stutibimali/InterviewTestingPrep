# Final integrated assessment, Part 3

Part 3 is another 45-minute debugging exercise with fresh logic and API cases.

Run it with:

```powershell
.\.venv\Scripts\python.exe -m pytest final_assessment_part3 -q
```

## Topics

- Whitespace normalization and string comparisons
- Retry sequences and maximum caps
- Non-mutating dictionary projections
- Datetime and nested Pydantic validation
- `202 Accepted` job execution
- `404 Not Found` for missing jobs
- Query limits and `422 Unprocessable Entity`

The schedule model is included as a reasoning prompt: inspect nearby validation
logic when the endpoint behavior appears correct but a model contract is wrong.