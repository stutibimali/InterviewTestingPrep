# Round 2 question set

Use this for timed practice rounds.

## 1. Environment / config
- The app reads `APP_ENV`, but the code checks `ENV` instead. What is happening and how do you fix it?

## 2. Data mutation bug
- A helper updates a list in place and later code unexpectedly sees the mutated values. How do you isolate and fix the bug?

## 3. Validation bug
- A Pydantic model rejects valid JSON because it expects int but receives a string-like number. What is the real issue?

## 4. Numeric bug
- A total is always off by a small margin. The values look correct in the UI but wrong in the API. What likely caused it?

## 5. API route bug
- A route returns 200 for invalid input because the function catches the exception and returns a generic payload. How do you fix the response contract?

## 6. Python logic bug
- A function should return the last repeated value, but it returns the first. Why? Explain the logic bug.

## 7. Type bug
- A helper uses `isinstance(value, str)` but fails for subclassed string objects. Why might this happen in production?

## 8. Null-handling bug
- A route crashes when a nested field is missing. What assumption is broken and how do you guard against it?

## 9. Hidden state bug
- A function returns different results based on earlier calls, even with the same input. What is mutating and how do you fix it?

## 10. Response schema bug
- The API returns data in the correct shape, but the model says it is invalid. What is likely mismatched?

## 11. Boundary bug
- The API should allow 10 but rejects 10 and accepts 11. Explain the off-by-one issue.

## 12. Serialization bug
- A response contains Decimal values and breaks JSON serialization. What is the exact fix?

## 13. List bug
- A function intended to return unique values actually removes valid items when duplicates appear. Find the root cause.

## 14. Conversion bug
- A request includes `"1"` and the service should treat it as 1, but it fails validation. Why is this happening?

## 15. Error handling bug
- A route catches all exceptions and hides the real error message. How do you preserve useful debugging information while keeping the API safe?

## 16. Async / sync bug
- A code path appears to work in sync tests but fails under async request handling. What is the likely issue in the execution model?

## 17. Path issue
- A helper builds URLs by string concatenation and generates malformed links when slashes are present. What is the real fix?

## 18. Sorting bug
- The app sorts by value but expects the order of original insertion. Why do results differ?

## 19. Enum bug
- A field is validated against a set of allowed values, but a value with different casing is still accepted. Why?

## 20. Security / config bug
- The app uses a hard-coded secret in a helper, but production should read from environment. How do you redesign it?

## Interview approach

For each scenario:
1. Read the symptom
2. Identify the failing input
3. Check assumptions
4. Fix the root cause
5. Validate with a focused test

This is the pattern most live debugging interviews are looking for.
