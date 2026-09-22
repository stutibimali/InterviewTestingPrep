from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "fastapi-debug-lab"}


def test_calculate_multiply() -> None:
    response = client.post(
        "/calculate",
        json={"first": 6, "second": 7, "operation": "multiply"},
    )
    assert response.status_code == 200
    assert response.json()["result"] == 42


def test_calculate_rejects_unknown_operation() -> None:
    response = client.post(
        "/calculate",
        json={"first": 6, "second": 7, "operation": "modulo"},
    )
    assert response.status_code == 422


def test_validation_error_scenario() -> None:
    response = client.get("/debug/validation-error", params={"value": 99})
    assert response.status_code == 422
    assert response.json()["detail"][0]["type"] == "less_than_equal"


def test_runtime_error_scenario() -> None:
    with TestClient(app, raise_server_exceptions=False) as isolated_client:
        response = isolated_client.get("/debug/runtime-error?trigger=true")
    assert response.status_code == 500
    assert "Internal Server Error" in response.text


def test_runtime_error_scenario_is_safe_by_default() -> None:
    response = client.get("/debug/runtime-error")
    assert response.status_code == 200
