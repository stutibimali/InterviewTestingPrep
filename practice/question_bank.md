# Large interview debugging question bank

This file gives you a broad set of realistic Python/FastAPI/Pydantic debugging prompts for mock interviews.

## Section A: Python fundamentals

1. A function returns the wrong max value when the list contains negative numbers.
2. A function is supposed to remove duplicates while preserving order, but it reorders items.
3. A string parser drops the final character when the input ends with whitespace.
4. A helper returns the wrong result for empty input instead of handling the edge case safely.
5. A list comprehension silently converts values incorrectly because of type coercion.
6. A dictionary helper merges nested configs but loses one of the inner keys.
7. A function is intended to check for palindrome strings but fails on mixed-case input.
8. A sorting function sorts strings lexicographically instead of by numeric value.
9. A loop exits early and never checks the final element in the sequence.
10. A recursion helper fails on a large input because it never handles a base case correctly.
11. A function returns None for a valid value because of a truthiness bug.
12. A date parser accepts invalid dates and returns a misleading output.

## Section B: FastAPI and request handling

13. A POST endpoint accepts quantity 0 when it should reject it with 422.
14. A route returns 500 instead of 400 when a required body field is missing.
15. A GET endpoint ignores the query parameter and returns the same static data each time.
16. An endpoint accidentally returns a string instead of JSON and breaks client code.
17. An API route returns 200 even when the request is invalid because validation is skipped.
18. A route relies on incorrect status-code handling and sends 201 for failed operations.
19. A route merges request body values but drops nested fields from the payload.
20. A parameter is declared as int but accepts a string because of invalid type coercion.
21. A schema field is optional in code but actually required at runtime because of default behavior.
22. A response model exposes the wrong field name, causing mismatches with the frontend.

## Section C: Pydantic and validation

23. A Pydantic model allows negative age values but should restrict them.
24. Email validation silently accepts malformed strings.
25. A model field is typed as float but receives int values that should be validated differently.
26. A nested model rejects valid payloads because the nested field is marked incorrectly.
27. A Union field chooses the wrong branch when more than one type matches.
28. A constrained field uses GT but should use GE, so boundary values are incorrectly accepted.
29. A dataclass-like field is validated without conversion, causing inconsistent behavior.
30. A custom validator runs too late and allows invalid values to pass.

## Section D: Debugging interviews and reasoning

31. The application starts but the route never responds because the app is bound to the wrong host or port.
32. A crash occurs only in production because environment variables are not loaded correctly.
33. The code works in tests but fails in a real request because of hidden assumptions about input shape.
34. A function behaves correctly for one dataset but fails for another due to mutation of shared state.
35. A route returns a valid payload but the frontend fails because the field names differ from the expected contract.
36. A helper accepts None but later calls a method on it, causing an unexpected runtime error.
37. A bug appears only after several operations because a previous call mutated global state.
38. A failing endpoint is related to a model default, not the route logic itself.
39. A schema mismatch causes `422` even though the request data is semantically correct.
40. A function appears correct but fails because it compares values using the wrong type or operator.

## Extra speaking points for the interview

When you approach these questions, explain:

- how you reproduce the failure,
- what specific input triggers it,
- what assumption is wrong,
- what minimal fix addresses the root cause,
- how you verify the fix with the smallest relevant test.

Good answers sound like a clear debugging workflow, not just a code patch.
