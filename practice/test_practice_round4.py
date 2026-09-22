import pytest
from fastapi.testclient import TestClient

from practice.challenge_api import app as calculator_app
from practice.challenge_environment import get_base_url
from practice.challenge_validation_and_models import app as validation_app


@pytest.mark.parametrize(
    ("key", "value"),
    [
        ("APP_ENV", "production"),
        ("ENV", "staging"),
        ("BASE_URL", "https://api.example.test"),
    ],
)
def test_environment_value_is_read_from_config_key(monkeypatch, key, value):
    monkeypatch.delenv("APP_ENV", raising=False)
    monkeypatch.delenv("ENV", raising=False)
    monkeypatch.delenv("BASE_URL", raising=False)
    monkeypatch.setenv(key, value)
    assert get_base_url() == value


def test_route_rejects_zero_quantity_validation():
    client = TestClient(validation_app)
    response = client.post(
        "/orders", json={"product": "widget", "quantity": 0, "price": 20.0}
    )
    assert response.status_code == 422


def test_route_rejects_negative_age_validation():
    client = TestClient(validation_app)
    response = client.post(
        "/profiles", json={"email": "a@example.com", "age": -1, "role": "admin"}
    )
    assert response.status_code == 422


def test_calculator_supports_subtract_operation():
    client = TestClient(calculator_app)
    response = client.post(
        "/calculate", json={"first": 10, "second": 4, "operation": "subtract"}
    )
    assert response.status_code == 200
    assert response.json() == {"result": 6}


def test_calculator_rejects_unknown_operation():
    client = TestClient(calculator_app)
    response = client.post(
        "/calculate", json={"first": 5, "second": 2, "operation": "modulo"}
    )
    assert response.status_code == 422


def test_calculator_uses_default_operation_when_not_provided():
    client = TestClient(calculator_app)
    response = client.post("/calculate", json={"first": 2, "second": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 5}


@pytest.mark.parametrize(
    "value",
    [
        "", "   ", None,
    ],
)
def test_valid_user_profile_requires_non_empty_email(value):
    client = TestClient(validation_app)
    payload = {"email": value, "age": 30, "role": "user"}
    response = client.post("/profiles", json=payload)
    assert response.status_code == 422


def test_nested_config_merge_keeps_base_values():
    from practice.challenge_data_transform import merge_settings

    base = {"db": {"host": "localhost", "port": 5432}, "debug": False}
    override = {"db": {"port": 5433}, "debug": True}
    assert merge_settings(base, override) == {
        "db": {"host": "localhost", "port": 5433},
        "debug": True,
    }


def test_total_reduces_decimal_values_correctly():
    from practice.challenge_data_transform import calculate_total

    items = [{"price": 10.5}, {"price": 2.25}, {"price": 7.5}]
    assert calculate_total(items) == 20.25


@pytest.mark.parametrize(
    "payload",
    [
        {"product": "widget", "quantity": 1, "price": "9.99"},
        {"product": "widget", "quantity": 2, "price": 10},
    ],
)
def test_order_price_accepts_numeric_types(payload):
    client = TestClient(validation_app)
    response = client.post("/orders", json=payload)
    assert response.status_code == 200


@pytest.mark.parametrize(
    "value",
    [
        0,
        -1,
        -100,
    ],
)
def test_order_quantity_is_positive(value):
    client = TestClient(validation_app)
    response = client.post(
        "/orders", json={"product": "widget", "quantity": value, "price": 20.0}
    )
    assert response.status_code == 422


@pytest.mark.parametrize(
    "age",
    [
        0,
        -1,
        -99,
    ],
)
def test_profile_age_is_positive(age):
    client = TestClient(validation_app)
    response = client.post(
        "/profiles", json={"email": "a@example.com", "age": age, "role": "user"}
    )
    assert response.status_code == 422


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        (12, 3, 4),
        (9, 3, 3),
        (-12, 3, -4),
    ],
)
def test_division_works_for_valid_values(left, right, expected):
    from practice.challenge_python_helpers import safe_divide

    assert safe_divide(left, right) == expected


@pytest.mark.parametrize(
    ("left", "right"),
    [(12, 0), (0, 0), (-12, 0)],
)
def test_division_returns_none_for_zero_divisor(left, right):
    from practice.challenge_python_helpers import safe_divide

    assert safe_divide(left, right) is None


def test_order_quantity_default_is_valid():
    client = TestClient(validation_app)
    response = client.post("/orders", json={"product": "widget"})
    assert response.status_code == 200
    assert response.json() == {"product": "widget", "quantity": 1, "price": 0.0}
