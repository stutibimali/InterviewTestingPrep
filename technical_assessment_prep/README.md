# Technical Assessment Prep for EY-style Python Debugging

This folder is built to match the kind of live debugging round described in the EY interview email:

- 45-minute live coding exercise
- Python + FastAPI + Pydantic concepts
- debugging existing code, not building from scratch
- explain reasoning while working
- focus on fundamentals, not speed

## Objectives

Practice the skills most likely to be tested:

- falsey values vs missing values
- request validation and bad input handling
- list and string parsing logic
- edge cases in loops and windowing logic
- FastAPI response/status handling
- writing clear, minimal fixes without overengineering

## Suggested workflow

1. Read the debug questions in `debug_questions.md`.
2. Run the tests in `test_technical_assessment_prep.py`.
3. Fix the code in the challenge files without using AI tooling.
4. Explain each fix out loud as if you're in the interview.

## Commands

```powershell
.\.venv\Scripts\python.exe -m pytest technical_assessment_prep -q
```

## Interview mindset

- Read the error carefully.
- Trace the data flow.
- Make one fix at a time.
- Keep the patch small and explainable.
- Validate with the smallest relevant test.
