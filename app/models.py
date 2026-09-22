from pydantic import BaseModel, Field


class CalculationRequest(BaseModel):
    first: float = Field(..., description="First operand")
    second: float = Field(..., description="Second operand")
    operation: str = Field(..., pattern="^(add|subtract|multiply|divide)$")


class CalculationResponse(BaseModel):
    first: float
    second: float
    operation: str
    result: float


class HealthResponse(BaseModel):
    status: str
    service: str


class DebugScenarioResponse(BaseModel):
    scenario: str
    detail: str
