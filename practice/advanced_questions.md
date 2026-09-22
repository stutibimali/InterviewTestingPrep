# Advanced interview debugging practice

Use these as extra questions for your mock interview prep. Each one is designed to simulate a small Python/FastAPI bug that shows up in live debugging exercises.

## 1) Environment bug
Question: A config helper returns the wrong value when the environment contains `API_BASE_URL=https://api.example.com/v1`.
Why it fails: The function strips the scheme and loses required information.

## 2) First unique item
Question: The function `first_unique()` returns the wrong element for repeated values.
Why it fails: It exits before evaluating the full list and uses the wrong tracking logic.

## 3) Missing number detection
Question: The function `find_missing_number()` fails on a sequence with a missing value in the middle.
Why it fails: It tests the wrong comparator and returns a wrong index.

## 4) Validation boundary
Question: A FastAPI route accepts zero or negative quantities.
Why it fails: The Pydantic model has no positive-number constraint.

## 5) Pricing and totals
Question: The total is incorrect when multiple line items are added.
Why it fails: The function drops decimals or sums strings instead of numbers.

## 6) Deep merge logic
Question: A settings merge function overwrites nested config incorrectly.
Why it fails: It performs a shallow merge instead of recursively merging nested dictionaries.

## 7) Division safety
Question: A calculator raises a confusing error when dividing by zero.
Why it fails: The function does not guard against zero before doing the division.

## 8) Response model mismatch
Question: An API returns a dictionary that is structurally valid but violates the response model.
Why it fails: Field names, aliases, or types do not match the expected schema.

## 9) Enum-like behavior
Question: A request with an unsupported status value is accepted even though it should be rejected.
Why it fails: Validation is not constrained to a set of allowed values.

## 10) Path normalization
Question: The route helper returns a wrong URL when inputs include leading/trailing slashes.
Why it fails: It strips and re-adds parts incorrectly.

## 11) Type confusion
Question: The function accepts strings where integers are expected.
Why it fails: The code uses loose type checks and does not convert or validate input.

## 12) False success path
Question: A helper says the value is valid even when it is None or empty.
Why it fails: A truthiness check hides the real problem.

## Practice rule
When debugging, do this in order:

1. Reproduce the failing test.
2. Read the stack trace and exact assertion.
3. Check the input and assumptions.
4. Fix the root cause, not the symptom.
5. Re-run the smallest relevant test.

This is the same approach interviewers look for in a live coding exercise.
