from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Round 3 Dispatch API")


class DispatchRequest(BaseModel):
    tracking_code: str = Field(min_length=6)
    destination: str
    packages: int = Field(gt=0)


@app.post("/dispatches", status_code=201)
def create_dispatch(request: DispatchRequest):
    return {
        "tracking_code": request.tracking_code,
        "destination": request.destination,
        "packages": int(request.packages),
        #"packages": str(request.packages),
    }


@app.get("/dispatches/{tracking_code}")
def get_dispatch(tracking_code: str):
    return {"tracking_code": tracking_code.upper(), "state": "queued"}