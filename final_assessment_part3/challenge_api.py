from datetime import datetime

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field, model_validator

app = FastAPI(title="Final Assessment Part 3 API")


class Schedule(BaseModel):
    starts_at: datetime
    ends_at: datetime

    @model_validator(mode="after")
    def ends_after_start(self):
        if self.starts_at > self.ends_at:
            raise ValueError("ends_at must be after starts_at")
        return self


class RunRequest(BaseModel):
    force: bool = False


@app.post("/jobs/{job_id}/run", status_code=202)
def run_job(job_id: str, request: RunRequest):
    if job_id == "missing":
        raise HTTPException(
            status_code=404,detail= "job not found"
            )
    return {"job_id": job_id, "state": "running", "force": request.force}


@app.get("/events")
def list_events(limit: int = Query(default=20, ge=1, le=100)):
    return {"items": [], "limit": limit}