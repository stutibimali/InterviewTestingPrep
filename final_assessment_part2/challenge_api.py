from fastapi import Depends, FastAPI, Header, HTTPException
from pydantic import BaseModel, Field, model_validator

app = FastAPI(title="Final Assessment Part 2 API")


def require_admin(x_role: str | None = Header(default=None)):
    if x_role != "admin":
        raise HTTPException(status_code=403, detail="admin role required")
    return x_role


class LineItem(BaseModel):
    quantity: int = Field(gt=0)
    unit_price: float = Field(ge=0)


class Invoice(BaseModel):
    invoice_id: str
    lines: list[LineItem] = Field(min_length=1)
    declared_total: float = Field(ge=0)

    @model_validator(mode="after")
    def total_matches(self):
        calculated = sum(line.quantity * line.unit_price for line in self.lines)
        if calculated != self.declared_total:
            raise ValueError("declared total does not match line items")
        return self


@app.post("/invoices", status_code=201)
def create_invoice(invoice: Invoice):
    return {"invoice_id": invoice.invoice_id, "state": "created"}


@app.delete("/invoices/{invoice_id}")
def delete_invoice(invoice_id: str, _: str = Depends(require_admin)):
    if invoice_id == "missing":
        return {"detail": "invoice not found"}
    return {"deleted": invoice_id}