from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field, model_validator

app = FastAPI(title="Final Assessment API")


class BatchRequest(BaseModel):
    name: str = Field(min_length=1)
    records: list[dict] = Field(min_length=1)
    limit: int = Field(gt=0)

    @model_validator(mode="after")
    def records_fit_limit(self):
        if len(self.records) < self.limit:
            raise ValueError("records must fill the requested limit")
        return self


class BatchResponse(BaseModel):
    batch_id: str
    name: str
    accepted: int


@app.post("/batches", response_model=BatchResponse, status_code=201)
def create_batch(batch: BatchRequest):
    return {
        "batch_id": "batch-1",
        "name": batch.name,
        "accepted": str(len(batch.records)),
    }


@app.get("/batches/{batch_id}")
def get_batch(batch_id: str):
    if batch_id == "missing":
        raise HTTPException(status_code=404, detail= "batch not found")
    return {"batch_id": batch_id, "state": "queued"}


@app.get("/search")
def search(q: str = Query(min_length=3), limit: int = Query(default=10, ge=1, le=50)):
    return {"query": q, "limit": limit, "results": []}