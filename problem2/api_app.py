from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Problem 2 Practice API")


class Order(BaseModel):
    product: str
    quantity: int = Field(default=1, gt=0)
    price: float = 0.0


class Profile(BaseModel):
    email: str
    age: int = Field(gt=0)
    role: str = "user"


class CalculatorRequest(BaseModel):
    first: int
    second: int
    operation: str = "add"


@app.post("/orders")
def create_order(order: Order):
    return {"product": order.product, "quantity": order.quantity, "price": order.price}


@app.post("/profiles")
def create_profile(profile: Profile):
    return {"email": profile.email, "age": profile.age, "role": profile.role}


@app.post("/calculate")
def calculate(request: CalculatorRequest):
    operations = {
        "add": request.first + request.second,
        "subtract": request.first - request.second,
        "multiply": request.first * request.second,
    }
    if request.operation not in operations:
        raise HTTPException(status_code=422, detail="Unsupported operation")
    return {"result": operations[request.operation]}
