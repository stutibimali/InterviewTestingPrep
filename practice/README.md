# Practice debugging exercises

This folder contains interview-style debugging challenges inspired by a FastAPI + Pydantic Python exercise.

Each challenge is intentionally broken in a realistic way. Your goal is to:

1. Read the question.
2. Reproduce the failure.
3. Trace the bug to the root cause.
4. Fix the code and validate it.

Recommended flow:

- Start from the question list in `questions.md`.
- Open a challenge file and read the bug description.
- Run `pytest practice -q` to see the failing checks.
- Fix the smallest root cause.
- Re-run the targeted tests.

## Interview practice matrix

`test_practice_interview.py` adds boundary-focused checks across all seeded challenge
families. The tests are expected to fail before you debug the challenge files. Use
the failure output as your prompt:

```powershell
.\.venv\Scripts\python.exe -m pytest practice\test_practice_interview.py -q
```

For a 45-minute mock interview, choose one failure from each area, explain the
observed behavior before editing, and run only the narrowest relevant test after
each change. A passing test means that one behavior is fixed; it does not mean the
whole practice set is complete.

The workspace agent `.github/agents/fastapi-debug-practice.agent.md` can facilitate
guided, timed, review, and short-drill practice sessions. Do not use it during an
assessment that prohibits AI assistance.

These exercises are intentionally created to be debugged locally, without using AI tools.
