import pytest
from fastapi.testclient import TestClient

from problem2.api_app import app


@pytest.mark.parametrize(
    ("payload", "expected_status"),
    [
        ({"product": "widget", "quantity": 1, "price": 9.99}, 200),
        ({"product": "widget", "quantity": 0, "price": 9.99}, 422),
        ({"product": "widget", "quantity": -2, "price": 9.99}, 422),
    ],
)
def test_order_quantity_validation(payload, expected_status):
    client = TestClient(app)
    response = client.post("/orders", json=payload)
    assert response.status_code == expected_status


@pytest.mark.parametrize(
    ("payload", "expected_status"),
    [
        ({"email": "a@example.com", "age": 30, "role": "user"}, 200),
        ({"email": "", "age": 30, "role": "user"}, 422),
        ({"email": "a@example.com", "age": -1, "role": "user"}, 422),
    ],
)
def test_profile_validation(payload, expected_status):
    client = TestClient(app)
    response = client.post("/profiles", json=payload)
    assert response.status_code == expected_status


@pytest.mark.parametrize(
    ("operation", "expected_result"),
    [
        ("add", 13),
        ("subtract", -1),
        ("multiply", 42),
    ],
)
def test_calculator_operations(operation, expected_result):
    client = TestClient(app)
    response = client.post(
        "/calculate", json={"first": 6, "second": 7, "operation": operation}
    )
    assert response.status_code == 200
    assert response.json() == {"result": expected_result}


def test_calculator_rejects_unknown_operation():
    client = TestClient(app)
    response = client.post(
        "/calculate", json={"first": 6, "second": 7, "operation": "modulo"}
    )
    assert response.status_code == 422


def test_calculator_uses_default_add_operation():
    client = TestClient(app)
    response = client.post("/calculate", json={"first": 5, "second": 2})
    assert response.status_code == 200
    assert response.json() == {"result": 7}


@pytest.mark.parametrize(
    ("base", "override", "expected"),
    [
        ({"db": {"host": "localhost", "port": 5432}, "debug": False}, {"db": {"port": 5433}, "debug": True}, {"db": {"host": "localhost", "port": 5433}, "debug": True}),
        ({"a": {"b": 1}}, {"a": {"c": 2}}, {"a": {"b": 1, "c": 2}}),
    ],
)
def test_recursive_merge_keeps_existing_nested_values(base, override, expected):
    from problem2.core_logic import merge_settings

    assert merge_settings(base, override) == expected


@pytest.mark.parametrize(
    ("items", "expected"),
    [
        (["a", "b", "a", "c", "c", "d"], "b"),
        (["x", "x", "y", "z", "z"], "y"),
        (["same", "same", "only"], "only"),
    ],
)
def test_first_unique_returns_first_single_occurrence(items, expected):
    from problem2.core_logic import first_unique

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
def test_missing_number_detection(nums, expected):
    from problem2.core_logic import find_missing_number

    assert find_missing_number(nums) == expected


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        (10, 2, 5),
        (-12, 3, -4),
        (7.5, 2.5, 3.0),
    ],
)
def test_division_returns_expected_values(left, right, expected):
    from problem2.core_logic import safe_divide

    assert safe_divide(left, right) == expected


def test_division_by_zero_returns_none():
    from problem2.core_logic import safe_divide

    assert safe_divide(10, 0) is None


def test_url_normalization_removes_duplicate_slashes():
    from problem2.core_logic import normalize_url

    assert normalize_url("https://example.com/", "/api/v1/") == "https://example.com/api/v1/"
