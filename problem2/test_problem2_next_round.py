import pytest
from fastapi.testclient import TestClient

from problem2.api_app import app


@pytest.mark.parametrize(
    ("payload", "expected_status"),
    [
        ({"product": "widget", "quantity": 1, "price": 10.0}, 200),
        ({"product": "widget", "quantity": 0, "price": 10.0}, 422),
        ({"product": "widget", "quantity": -5, "price": 10.0}, 422),
    ],
)
def test_order_validates_quantity(payload, expected_status):
    client = TestClient(app)
    response = client.post("/orders", json=payload)
    assert response.status_code == expected_status


@pytest.mark.parametrize(
    ("payload", "expected_status"),
    [
        ({"email": "a@example.com", "age": 25, "role": "user"}, 200),
        ({"email": "", "age": 25, "role": "user"}, 422),
        ({"email": "a@example.com", "age": -1, "role": "user"}, 422),
    ],
)
def test_profile_validates_input(payload, expected_status):
    client = TestClient(app)
    response = client.post("/profiles", json=payload)
    assert response.status_code == expected_status


@pytest.mark.parametrize(
    ("operation", "expected"),
    [
        ("add", 9),
        ("subtract", 1),
        ("multiply", 14),
    ],
)
def test_calculator_operations(operation, expected):
    client = TestClient(app)
    response = client.post(
        "/calculate", json={"first": 7, "second": 2, "operation": operation}
    )
    assert response.status_code == 200
    assert response.json() == {"result": expected}


def test_calculator_rejects_unknown_operation():
    client = TestClient(app)
    response = client.post(
        "/calculate", json={"first": 7, "second": 2, "operation": "divide"}
    )
    assert response.status_code == 422


@pytest.mark.parametrize(
    ("items", "expected"),
    [
        (["a", "b", "a", "c", "c", "d"], "b"),
        (["x", "x", "y", "z", "z"], "y"),
        (["same", "same", "only"], "only"),
    ],
)
def test_first_unique(items, expected):
    from problem2.core_logic import first_unique

    assert first_unique(items) == expected


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        ([1, 2, 4, 5, 6], 3),
        ([1, 2, 3, 5, 6], 4),
        ([2, 3, 4, 5, 7], 1),
    ],
)
def test_missing_number(nums, expected):
    from problem2.core_logic import find_missing_number

    assert find_missing_number(nums) == expected


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([10, 2.5, 7], 19.5),
        ([1, 2, 3], 6),
        ([5, 5, 5], 15),
    ],
)
def test_total_without_tax(values, expected):
    from problem2.core_logic import total_without_tax

    assert total_without_tax(values) == expected


@pytest.mark.parametrize(
    ("base", "override", "expected"),
    [
        ({"db": {"host": "localhost", "port": 5432}, "debug": False}, {"db": {"port": 5433}, "debug": True}, {"db": {"host": "localhost", "port": 5433}, "debug": True}),
        ({"a": {"b": 1}}, {"a": {"c": 2}}, {"a": {"b": 1, "c": 2}}),
    ],
)
def test_recursive_merge(base, override, expected):
    from problem2.core_logic import merge_settings

    assert merge_settings(base, override) == expected


def test_url_normalization():
    from problem2.core_logic import normalize_url

    assert normalize_url("https://example.com/", "/api/v1/") == "https://example.com/api/v1/"


def test_safe_divide_zero():
    from problem2.core_logic import safe_divide

    assert safe_divide(10, 0) is None
