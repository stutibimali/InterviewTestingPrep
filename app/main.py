from fastapi import FastAPI, Query

from app.calculator import calculate
from app.models import (
    CalculationRequest,
    CalculationResponse,
    DebugScenarioResponse,
    HealthResponse,
)

app = FastAPI(title="FastAPI Debug Lab", version="0.1.0")


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok", service="fastapi-debug-lab")


@app.post("/calculate", response_model=CalculationResponse)
def calculate_route(request: CalculationRequest) -> CalculationResponse:
    result = calculate(request.first, request.second, request.operation)
    return CalculationResponse(
        first=request.first,
        second=request.second,
        operation=request.operation,
        result=result,
    )


@app.get("/debug/validation-error", response_model=DebugScenarioResponse)
def validation_error_scenario(
    value: int = Query(..., ge=1, le=10, description="Use 1 through 10")
) -> DebugScenarioResponse:
    return DebugScenarioResponse(
        scenario="validation-error",
        detail=f"Validated value: {value}",
    )


@app.get("/debug/runtime-error", response_model=DebugScenarioResponse)
def runtime_error_scenario(
    trigger: bool = Query(False, description="Set true to raise the intentional error")
) -> DebugScenarioResponse:
    if trigger:
        raise RuntimeError("Intentional runtime failure for debugger practice")
    return DebugScenarioResponse(
        scenario="runtime-error",
        detail="Set trigger=true to pause on the intentional RuntimeError.",
    )
