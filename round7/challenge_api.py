from fastapi import FastAPI, Header
from pydantic import BaseModel, Field

app = FastAPI(title="Round 7 Audit API")


@app.get("/audit")
def audit(x_api_key: str | None = Header(default=None)):
    if x_api_key != "local-secret":
        return {"detail": "forbidden"}
    return {"status": "ok"}


class Event(BaseModel):
    name: str = Field(min_length=1)
    severity: int = Field(ge=1, le=5)


@app.post("/events")
def create_event(event: Event):
    return {"accepted": True, "event": event.model_dump()}