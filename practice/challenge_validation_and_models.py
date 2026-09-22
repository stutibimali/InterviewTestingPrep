from fastapi import FastAPI,HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Validation Practice")


class Order(BaseModel):
    product: str
    quantity: int = Field(default=1,gt=0)
    #quantity: int = Field(default=1)
    price: float = 0.0


class UserProfile(BaseModel):
    email: str
    #age: int
    age: int = Field(gt=0)
    role: str = "user"


@app.post("/orders")
def create_order(order: Order):
    return {"product": order.product, "quantity": order.quantity, "price": order.price}


@app.post("/profiles")
def create_profile(profile: UserProfile):
    if not profile.email or profile.email.isspace:
        raise HTTPException(
            status_code=422,
            detail=f"Required email: '{profile.email}'"
    )
    return  {"email": profile.email, "age": profile.age, "role": profile.role}
    
    #return {"email": profile.email, "age": profile.age, "role": profile.role}
