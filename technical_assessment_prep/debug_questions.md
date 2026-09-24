# EY-style debugging questions

These are representative of a technical assessment in a live coding interview.

## Question 1: Falsey values

A function is supposed to use a fallback value only when the passed value is missing (`None`), not when it is a valid falsey value like `0` or an empty string.

Common bug:

```python
return value or fallback
```

Why it fails:
- `0` becomes fallback
- `""` becomes fallback
- these are valid values and should stay untouched

## Question 2: CSV parsing

A config value may include a comma-separated list with whitespace and empty entries.

Expected behavior:
- trim each item
- remove empty strings
- keep clean values only

## Question 3: Sliding windows

The function should return all valid consecutive windows of a given width, including the last possible one.

Example:
- input: `[1, 2, 3, 4]`, width `3`
- expected: `[[1,2,3], [2,3,4]]`

Common bug:
- `range(len(values) - width)` excludes the last valid window

## Question 4: API validation

A FastAPI endpoint should reject unsupported roles and return `403`.

Expected values:
- allowed roles: `reader`, `editor`
- anything else: reject

## Question 5: Data normalization

A helper should normalize names by trimming whitespace and removing empty values without dropping valid content.

## Question 6: Pydantic model behavior

A data model should validate required fields and reject missing values, while still allowing optional values where appropriate.

## Interview talking points

When you solve these, narrate your process:

1. Identify the actual failing behavior.
2. Check the edge condition causing it.
3. Apply the smallest root-cause fix.
4. Run the relevant test.
5. Explain why the fix is correct.
