#from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Practice API")


class Order(BaseModel):
    product: str
    quantity: int = Field(default=1,gt=0)
    #quantity: int = Field(default=1)

class CalculatorRequest(BaseModel):
    first: int
    second: int
    operation: str = "add"


@app.post("/orders")
def create_order(order: Order):
    return {"product": order.product, "quantity": order.quantity}


@app.post("/calculate")
def calculate(request: CalculatorRequest):
    operation = {
            "add": request.first + request.second,
            "subtract": request.first - request.second,
            "multiply": request.first * request.second,
        } 
    if request.operation not in operation:
        raise HTTPException(
            status_code=422,
            detail=f"Unsupported operation: '{request.operation}'"
        )
    return {"result": operation[request.operation]}
    """operations = {
            "add": request.first + request.second,
            "subtract": request.first - request.second,
            "multiply": request.first * request.second,
        } 
    return {"result": operations.get(request.operation, "unsupported operation")}"""
