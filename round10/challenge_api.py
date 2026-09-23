from fastapi import FastAPI, Query

app = FastAPI(title="Round 10 Search API")


@app.get("/search")
def search(q: str = Query(min_length=2), limit: int = Query(default=10, ge=1, le=50)):
    return {"query": q, "limit": limit, "results": []}