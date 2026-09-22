import pytest
from fastapi.testclient import TestClient

from problem2.api_app import app
from problem2.core_logic import find_missing_number, first_unique, merge_settings, normalize_url, safe_divide


@pytest.mark.parametrize(
    ("items", "expected"),
    [
        (["a", "b", "a", "c", "c", "d"], "b"),
        ([1, 2, 3, 2, 1, 4], 3),
        (["x", "x", "y", "z", "z"], "y"),
        (["same", "same", "only"], "only"),
    ],
)
def test_first_unique_returns_first_non_duplicate(items, expected):
    assert first_unique(items) == expected


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        ([1, 2, 4, 5, 6], 3),
        ([2, 3, 4, 5, 7], 1),
        ([5, 6, 7, 8, 10], 9),
        ([1, 2, 3, 4], 5),
    ],
)
def test_find_missing_number_detects_gap(nums, expected):
    assert find_missing_number(nums) == expected


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        (10, 2, 5),
        (-12, 3, -4),
        (7.5, 2.5, 3.0),
    ],
)
def test_safe_divide_handles_valid_input(left, right, expected):
    assert safe_divide(left, right) == expected


@pytest.mark.parametrize(
    ("left", "right"),
    [(10, 0), (0, 0), (-5, 0)],
)
def test_safe_divide_returns_none_for_zero_divisor(left, right):
    assert safe_divide(left, right) is None


def test_normalize_url_removes_duplicate_slashes():
    assert normalize_url("https://example.com/", "/api/v1/") == "https://example.com/api/v1/"


def test_merge_settings_recursively_updates_nested_values():
    base = {"db": {"host": "localhost", "port": 5432}, "debug": False}
    override = {"db": {"port": 5433}, "debug": True}
    assert merge_settings(base, override) == {
        "db": {"host": "localhost", "port": 5433},
        "debug": True,
    }


def test_route_rejects_empty_email_string():
    client = TestClient(app)
    response = client.post(
        "/profiles", json={"email": "", "age": 30, "role": "user"}
    )
    assert response.status_code == 422


def test_route_rejects_zero_quantity():
    client = TestClient(app)
    response = client.post(
        "/orders", json={"product": "widget", "quantity": 0, "price": 20.0}
    )
    assert response.status_code == 422


def test_route_rejects_negative_age():
    client = TestClient(app)
    response = client.post(
        "/profiles", json={"email": "a@example.com", "age": -1, "role": "admin"}
    )
    assert response.status_code == 422


def test_route_accepts_valid_payload():
    client = TestClient(app)
    response = client.post(
        "/orders", json={"product": "widget", "quantity": 3, "price": 4.5}
    )
    assert response.status_code == 200
    assert response.json() == {"product": "widget", "quantity": 3, "price": 4.5}


def test_calculator_supports_subtract_and_multiply():
    client = TestClient(app)

    response = client.post(
        "/calculate", json={"first": 10, "second": 4, "operation": "subtract"}
    )
    assert response.status_code == 200
    assert response.json() == {"result": 6}

    response = client.post(
        "/calculate", json={"first": 10, "second": 4, "operation": "multiply"}
    )
    assert response.status_code == 200
    assert response.json() == {"result": 40}


def test_calculator_rejects_unknown_operation():
    client = TestClient(app)
    response = client.post(
        "/calculate", json={"first": 5, "second": 2, "operation": "modulo"}
    )
    assert response.status_code == 422


def test_calculator_defaults_to_add_when_operation_omitted():
    client = TestClient(app)
    response = client.post("/calculate", json={"first": 2, "second": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 5}


def test_order_default_quantity_is_valid():
    client = TestClient(app)
    response = client.post("/orders", json={"product": "widget", "price": 10.0})
    assert response.status_code == 200
    assert response.json() == {"product": "widget", "quantity": 1, "price": 10.0}
