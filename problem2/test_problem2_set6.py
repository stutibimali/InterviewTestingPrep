import pytest
from fastapi.testclient import TestClient

from problem2.api_app import app


@pytest.mark.parametrize(
    ("payload", "expected_status"),
    [
        ({"product": "pen", "quantity": 2, "price": 12.5}, 200),
        ({"product": "pen", "quantity": 0, "price": 12.5}, 422),
        ({"product": "pen", "quantity": -1, "price": 12.5}, 422),
    ],
)
def test_order_validation_round(payload, expected_status):
    client = TestClient(app)
    response = client.post("/orders", json=payload)
    assert response.status_code == expected_status


@pytest.mark.parametrize(
    ("payload", "expected_status"),
    [
        ({"email": "user@example.com", "age": 25, "role": "admin"}, 200),
        ({"email": "", "age": 25, "role": "admin"}, 422),
        ({"email": "user@example.com", "age": -1, "role": "admin"}, 422),
    ],
)
def test_profile_validation_round(payload, expected_status):
    client = TestClient(app)
    response = client.post("/profiles", json=payload)
    assert response.status_code == expected_status


@pytest.mark.parametrize(
    ("operation", "expected"),
    [
        ("add", 11),
        ("subtract", 1),
        ("multiply", 30),
    ],
)
def test_calculator_round(operation, expected):
    client = TestClient(app)
    response = client.post(
        "/calculate", json={"first": 5, "second": 6, "operation": operation}
    )
    assert response.status_code == 200
    assert response.json() == {"result": expected}


def test_unknown_operation_rejected_round():
    client = TestClient(app)
    response = client.post(
        "/calculate", json={"first": 10, "second": 2, "operation": "divide"}
    )
    assert response.status_code == 422


@pytest.mark.parametrize(
    ("items", "expected"),
    [
        (["a", "b", "a", "c", "c", "d"], "b"),
        ([1, 2, 3, 2, 1, 4], 3),
        (["x", "x", "y", "z", "z"], "y"),
    ],
)
def test_first_unique_round(items, expected):
    from problem2.core_logic import first_unique

    assert first_unique(items) == expected


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        ([1, 2, 4, 5, 6], 3),
        ([5, 6, 7, 8, 10], 9),
        ([2, 3, 4, 5, 7], 1),
    ],
)
def test_missing_number_round(nums, expected):
    from problem2.core_logic import find_missing_number

    assert find_missing_number(nums) == expected


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        (20, 4, 5),
        (-12, 3, -4),
        (7.5, 2.5, 3.0),
    ],
)
def test_safe_divide_round(left, right, expected):
    from problem2.core_logic import safe_divide

    assert safe_divide(left, right) == expected


def test_safe_divide_zero_round():
    from problem2.core_logic import safe_divide

    assert safe_divide(10, 0) is None


def test_normalize_url_round():
    from problem2.core_logic import normalize_url

    assert normalize_url("https://example.com/base/", "/users/profile") == (
        "https://example.com/base/users/profile"
    )


def test_total_without_tax_round():
    from problem2.core_logic import total_without_tax

    assert total_without_tax([10, 2.5, 7]) == 19.5


def test_merge_settings_round():
    from problem2.core_logic import merge_settings

    base = {"db": {"host": "localhost", "port": 5432}, "debug": False}
    override = {"db": {"port": 5433}, "debug": True}
    assert merge_settings(base, override) == {
        "db": {"host": "localhost", "port": 5433},
        "debug": True,
    }
