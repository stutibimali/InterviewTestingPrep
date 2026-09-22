import pytest
from fastapi.testclient import TestClient

from practice.challenge_api import app as calculator_app
from practice.challenge_core_python import first_unique as core_first_unique
from practice.challenge_data_transform import calculate_total, merge_settings
from practice.challenge_environment import get_base_url
from practice.challenge_python_helpers import (
    find_missing_number,
    first_unique as helper_first_unique,
    safe_divide,
)
from practice.challenge_validation_and_models import app as validation_app


@pytest.mark.parametrize(
    ("variable", "value"),
    [
        ("API_BASE_URL", "https://api.example.com/v1"),
        ("API_BASE_URL", "http://localhost:9000"),
        ("BASE_URL", "https://internal.example.test"),
    ],
)
def test_base_url_preserves_configured_value(monkeypatch, variable, value):
    monkeypatch.delenv("BASE_URL", raising=False)
    monkeypatch.delenv("API_BASE_URL", raising=False)
    monkeypatch.setenv(variable, value)
    assert get_base_url() == value


def test_base_url_prefers_base_url(monkeypatch):
    monkeypatch.setenv("BASE_URL", "https://primary.example.com")
    monkeypatch.setenv("API_BASE_URL", "https://fallback.example.com")
    assert get_base_url() == "https://primary.example.com"


def test_base_url_uses_default_when_unconfigured(monkeypatch):
    monkeypatch.delenv("BASE_URL", raising=False)
    monkeypatch.delenv("API_BASE_URL", raising=False)
    assert get_base_url() == "http://localhost:8000"


@pytest.mark.parametrize(
    "items, expected",
    [
        (["a", "b", "a", "c", "c", "d"], "b"),
        ([1, 2, 3, 2, 1, 4], 3),
        (["x", "x", "y"], "y"),
        (["x", "x"], None),
        ([], None),
    ],
)
def test_core_first_unique_returns_first_item_with_one_occurrence(items, expected):
    assert core_first_unique(items) == expected


@pytest.mark.parametrize(
    "items, expected",
    [
        (["a", "b", "a", "c", "c", "d"], "b"),
        ([1, 2, 3, 2, 1, 4], 3),
        (["same", "same", "only"], "only"),
        ([], None),
    ],
)
def test_helper_first_unique_returns_first_item_with_one_occurrence(items, expected):
    assert helper_first_unique(items) == expected


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 4, 5, 6], 3),
        ([2, 3, 4, 5, 7], 1),
        ([1, 2, 3, 4], 5),
        ([2], 1),
    ],
)
def test_find_missing_number_handles_boundaries(nums, expected):
    assert find_missing_number(nums) == expected


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [(10, 2, 5), (10, 0, None), (-9, 3, -3), (0, 5, 0)],
)
def test_safe_divide_returns_none_only_for_zero_divisor(left, right, expected):
    assert safe_divide(left, right) == expected


def test_calculate_total_handles_integer_and_decimal_prices():
    assert calculate_total([{"price": 10}, {"price": 2.25}, {"price": "7.5"}]) == 19.75


def test_calculate_total_handles_empty_items():
    assert calculate_total([]) == 0


def test_merge_settings_does_not_mutate_inputs():
    base = {"db": {"host": "localhost", "port": 5432}, "debug": False}
    override = {"db": {"port": 5433}, "debug": True}
    merge_settings(base, override)
    assert base == {"db": {"host": "localhost", "port": 5432}, "debug": False}
    assert override == {"db": {"port": 5433}, "debug": True}


def test_merge_settings_recursively_merges_nested_values():
    base = {"db": {"host": "localhost", "port": 5432}, "debug": False}
    override = {"db": {"port": 5433}, "debug": True}
    assert merge_settings(base, override) == {
        "db": {"host": "localhost", "port": 5433},
        "debug": True,
    }


@pytest.fixture
def validation_client():
    return TestClient(validation_app)


@pytest.mark.parametrize("quantity", [0, -1, -100])
def test_orders_reject_non_positive_quantity(validation_client, quantity):
    response = validation_client.post(
        "/orders", json={"product": "widget", "quantity": quantity, "price": 20.0}
    )
    assert response.status_code == 422


def test_orders_accept_positive_quantity_and_default_price(validation_client):
    response = validation_client.post("/orders", json={"product": "widget", "quantity": 2})
    assert response.status_code == 200
    assert response.json() == {"product": "widget", "quantity": 2, "price": 0.0}


@pytest.mark.parametrize("age", [0, -1, -99])
def test_profiles_reject_non_positive_age(validation_client, age):
    response = validation_client.post(
        "/profiles", json={"email": "a@example.com", "age": age}
    )
    assert response.status_code == 422


def test_profiles_default_role_is_user(validation_client):
    response = validation_client.post(
        "/profiles", json={"email": "a@example.com", "age": 30}
    )
    assert response.status_code == 200
    assert response.json()["role"] == "user"


@pytest.fixture
def calculator_client():
    return TestClient(calculator_app)


@pytest.mark.parametrize(
    ("operation", "expected"),
    [("add", 13), ("subtract", -1), ("multiply", 42)],
)
def test_calculator_supports_each_operation(calculator_client, operation, expected):
    response = calculator_client.post(
        "/calculate", json={"first": 6, "second": 7, "operation": operation}
    )
    assert response.status_code == 200
    assert response.json() == {"result": expected}


def test_calculator_rejects_unknown_operation(calculator_client):
    response = calculator_client.post(
        "/calculate", json={"first": 6, "second": 7, "operation": "modulo"}
    )
    assert response.status_code == 422


def test_calculator_uses_add_as_the_default_operation(calculator_client):
    response = calculator_client.post("/calculate", json={"first": 6, "second": 7})
    assert response.status_code == 200
    assert response.json() == {"result": 13}


def test_calculator_rejects_missing_operands(calculator_client):
    response = calculator_client.post("/calculate", json={"first": 6})
    assert response.status_code == 422