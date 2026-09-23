from final_assessment.challenge_api import app
from final_assessment.challenge_core import (
    calculate_total,
    load_limits,
    unique_in_order,
)
from fastapi.testclient import TestClient


def test_environment_json_is_loaded_as_integer_limits(monkeypatch):
    monkeypatch.setenv("LIMITS_JSON", '{"free": "10", "paid": 100}')

    assert load_limits() == {"free": 10, "paid": 100}


def test_unique_values_keep_input_order():
    assert unique_in_order(["b", "a", "b", "c"]) == ["b", "a", "c"]


def test_invoice_applies_tax_as_a_rate_after_discount():
    assert calculate_total([100.0], discount=0.1, tax=0.2) == 99.0


def test_batch_requires_enough_records_for_limit():
    response = TestClient(app).post(
        "/batches",
        json={"name": "import", "records": [{"id": 1}], "limit": 2},
    )

    assert response.status_code == 422


def test_batch_returns_created_response_with_numeric_count():
    response = TestClient(app).post(
        "/batches",
        json={"name": "import", "records": [{"id": 1}, {"id": 2}], "limit": 2},
    )

    assert response.status_code == 201
    assert response.json() == {
        "batch_id": "batch-1",
        "name": "import",
        "accepted": 2,
    }


def test_missing_batch_returns_not_found():
    response = TestClient(app).get("/batches/missing")

    assert response.status_code == 404


def test_search_requires_at_least_three_characters():
    response = TestClient(app).get("/search?q=ab")

    assert response.status_code == 422