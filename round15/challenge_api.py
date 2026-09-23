from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Round 15 Profiles API")


class Profile(BaseModel):
    username: str
    active: bool


@app.get("/profiles/{username}", response_model=Profile)
def get_profile(username: str):
    return {"username": username, "active": True, "internal": "hidden"}