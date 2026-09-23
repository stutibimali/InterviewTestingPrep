from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Round 6 Accounts API")


class AccountResponse(BaseModel):
    account_id: str
    display_name: str
    active: bool


@app.get("/accounts/{account_id}", response_model=AccountResponse)
def get_account(account_id: str):
    if account_id == "missing":
        return {"error": "account not found"}
    return {"account_id": account_id, "display_name": "Ada", "active": True}


class TransferRequest(BaseModel):
    amount: float = Field(gt=0)


@app.post("/accounts/{account_id}/transfer")
def transfer(account_id: str, request: TransferRequest):
    if account_id == "locked":
        raise HTTPException(status_code=409, detail="account is locked")
    return {"account_id": account_id, "amount": request.amount, "state": "accepted"}