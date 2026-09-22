# Problem 2 practice bank

This folder is a second, independent debugging set modeled on the same interview pattern as the main practice exercises.

## Most likely interview categories

These are the problem types that appear most often in this style of assessment:

1. Environment/config mismatch
2. Wrong Python logic or early-return bug
3. Validation boundary bug
4. Division-by-zero safety bug
5. Recursive merge bug
6. Numeric conversion / float truncation bug
7. API contract mismatch
8. Response validation bug
9. Missing or malformed nested data
10. Default value / type coercion issue

## How to use this folder

- Run one test file at a time.
- Read the failing assertion carefully.
- Do not guess. Trace the exact input.
- Fix only the root cause.
- Re-run the smallest relevant test.

## Interview mindset

The goal is not speed. The goal is to show a structured debugging workflow.

A strong answer sounds like:

- I reproduced the failing case.
- I identified the exact wrong assumption.
- I traced the bug to the relevant function.
- I fixed the root cause without broad changes.
- I verified the behavior with a focused test.
