from fastapi import FastAPI, Header, HTTPException

app = FastAPI(title="Round 16 Notes API")


@app.get("/notes")
def list_notes(x_role: str | None = Header(default=None)):
    if x_role not in {"reader", "editor"}:
        raise HTTPException(status_code=403, detail="unsupported role")
    return {"role": x_role, "notes": []}