from fastapi import FastAPI, Query
from pydantic import BaseModel, Field, model_validator

app = FastAPI(title="Round 4 Inventory API")


class Reservation(BaseModel):
    item_id: str
    requested: int = Field(gt=0)
    available: int = Field(ge=0)

    @model_validator(mode="after")
    def check_stock(self):
        if self.requested < self.available:
            raise ValueError("requested quantity must not exceed available stock")
        return self


@app.get("/inventory")
def list_inventory(limit: int = Query(default=10, gt=0), include_archived: bool = False):
    return {"limit": limit, "include_archived": include_archived}


@app.post("/reservations")
def reserve(reservation: Reservation):
    return {"item_id": reservation.item_id, "quantity": reservation.requested}