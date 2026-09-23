# Round 5 debugging practice

This round is independent from `practice/`, `problem2/`, `round3/`, and
`round4/`. The challenge files contain deliberate bugs and the tests define the
expected behavior.

Run it with:

```powershell
.\.venv\Scripts\python.exe -m pytest round5 -q
```

## Problem areas

- Split key-value text while allowing delimiters inside values.
- Include the final short batch when paginating a list.
- Handle `None` as well as malformed integers in an exception boundary.
- Serialize datetimes using their ISO representation.
- Apply API pagination as `offset: offset + limit`.
- Preserve explicit empty-string PATCH values instead of treating them as absent.

For interview practice, reproduce one failure at a time, identify the exact
input that triggers it, explain the root cause, and rerun the smallest test.