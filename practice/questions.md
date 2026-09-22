# Practice questions

## 1) Environment configuration
Question: Why does `get_base_url()` return an incorrect value even when `API_BASE_URL` is set in the environment?

Hints:
- Check the exact environment variable name.
- Check whether the function strips or mutates the value unexpectedly.

## 2) Core Python logic
Question: Why does `first_unique()` return the wrong element for duplicate-heavy input?

Hints:
- Trace the iteration order.
- Check whether the function exits too early.
- Confirm the correct definition of "first unique".

## 3) FastAPI validation
Question: Why does the API accept an invalid order quantity of 0 or a negative number?

Hints:
- Inspect the Pydantic model.
- Confirm whether validation constraints are actually applied.
- Check how the route handles invalid input.

## 4) API behavior
Question: Why does the calculator response return the wrong output for valid requests?

Hints:
- Confirm the operation mapping.
- Check whether the result is computed or transformed incorrectly.
- Compare the endpoint behavior against the expected JSON payload.
