from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Round 12 Files API")


class UploadReceipt(BaseModel):
    filename: str = Field(min_length=1)
    size: int = Field(ge=0)


@app.post("/uploads", response_model=UploadReceipt)
def create_upload(filename: str, size: int):
    return {"filename": filename, "size": size}