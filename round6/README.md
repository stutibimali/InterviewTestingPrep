# Round 6 debugging practice

This is an independent debugging set. It does not reuse the challenge cases from
`practice/`, `problem2/`, or rounds 3 through 5.

Run it with:

```powershell
.\.venv\Scripts\python.exe -m pytest round6 -q
```

## Problem areas

- Guarantee resource cleanup when an operation raises.
- Perform case-insensitive record lookup on both sides of the comparison.
- Reject invalid leaves while recursively flattening nested lists.
- Preserve explicit settings while applying defaults.
- Return an HTTP 404 instead of allowing response-model validation to hide the
  intended missing-resource behavior.
- Return the correct conflict status for a locked account.

Use the failing assertion as the contract, trace the smallest code path that
produces it, and rerun one focused test after each fix.