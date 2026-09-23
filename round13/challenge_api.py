from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Round 13 Metrics API")


class Metric(BaseModel):
    name: str
    value: float


@app.get("/health")
def health():
    return "ok"


@app.post("/metrics", response_model=Metric, status_code=201)
def create_metric(metric: Metric):
    return metric.model_dump()