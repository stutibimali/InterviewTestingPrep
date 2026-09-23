from fastapi import FastAPI, Query

app = FastAPI(title="Round 14 Preferences API")


@app.get("/preferences")
def preferences(
    page: int = Query(default=1, ge=1), compact: bool = Query(default=False)
):
    return {"page": page, "compact": compact}