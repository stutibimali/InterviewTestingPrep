from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Round 9 Jobs API")


class JobRequest(BaseModel):
    name: str = Field(min_length=1)
    priority: int = Field(ge=1, le=3)


@app.post("/jobs")
def create_job(request: JobRequest):
    return {"name": request.name, "priority": request.priority, "state": "queued"}


@app.get("/jobs/{job_id}")
def get_job(job_id: str):
    if job_id == "missing":
        return {"detail": "job not found"}
    return {"job_id": job_id, "state": "queued"}