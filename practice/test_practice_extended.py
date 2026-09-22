from fastapi.testclient import TestClient

from practice.challenge_data_transform import calculate_total, merge_settings
from practice.challenge_python_helpers import find_missing_number, first_unique, safe_divide
from practice.challenge_validation_and_models import app
from practice.challenge_environment import get_base_url


def test_get_base_url_keeps_https_scheme(monkeypatch):
    monkeypatch.setenv("API_BASE_URL", "https://api.example.com/v1")
    assert get_base_url() == "https://api.example.com/v1"


def test_first_unique_returns_first_non_duplicate():
    assert first_unique(["a", "b", "a", "c", "c", "d"]) == "b"
    assert first_unique([1, 2, 3, 2, 1, 4]) == 3


def test_find_missing_number_in_sequence():
    assert find_missing_number([1, 2, 4, 5, 6]) == 3
    assert find_missing_number([2, 3, 4, 5, 7]) == 6


def test_safe_divide_returns_none_for_zero_divisor():
    assert safe_divide(10, 2) == 5
    assert safe_divide(10, 0) is None


def test_order_quantity_must_be_positive():
    client = TestClient(app)
    response = client.post("/orders", json={"product": "widget", "quantity": 0, "price": 20.0})
    assert response.status_code == 422

    response = client.post("/orders", json={"product": "widget", "quantity": -2, "price": 20.0})
    assert response.status_code == 422


def test_profile_age_must_be_positive_integer():
    client = TestClient(app)
    response = client.post("/profiles", json={"email": "a@example.com", "age": -1, "role": "admin"})
    assert response.status_code == 422


def test_calculate_total_sums_prices_correctly():
    items = [{"price": 10.5}, {"price": 2.25}, {"price": 7.5}]
    assert calculate_total(items) == 20.25


def test_merge_settings_recursively_merges_nested_values():
    base = {"db": {"host": "localhost", "port": 5432}, "debug": False}
    override = {"db": {"port": 5433}, "debug": True}
    assert merge_settings(base, override) == {"db": {"host": "localhost", "port": 5433}, "debug": True}
