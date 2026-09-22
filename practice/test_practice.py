import os

import pytest
from fastapi.testclient import TestClient

from practice.challenge_api import app
from practice.challenge_core_python import first_unique
from practice.challenge_environment import get_base_url


# 1) Environment configuration

def test_get_base_url_uses_api_base_url(monkeypatch):
    monkeypatch.setenv("API_BASE_URL", "https://api.example.com/v1")
    assert get_base_url() == "https://api.example.com/v1"


# 2) Core Python logic

def test_first_unique_returns_first_non_duplicate():
    assert first_unique(["a", "b", "a", "c", "c", "d"]) == "b"
    assert first_unique([1, 2, 3, 2, 1, 4]) == 3


# 3) FastAPI validation

def test_order_quantity_must_be_positive():
    client = TestClient(app)
    response = client.post("/orders", json={"product": "widget", "quantity": 0})
    assert response.status_code == 422

    response = client.post("/orders", json={"product": "widget", "quantity": -2})
    assert response.status_code == 422


# 4) API behavior

def test_calculate_addition_and_multiplication():
    client = TestClient(app)

    response = client.post("/calculate", json={"first": 6, "second": 7, "operation": "add"})
    assert response.status_code == 200
    assert response.json() == {"result": 13}

    response = client.post("/calculate", json={"first": 6, "second": 7, "operation": "multiply"})
    assert response.status_code == 200
    assert response.json() == {"result": 42}


@pytest.mark.parametrize(
    ("items", "expected"),
    [
        (["x", "x", "y"], "y"),
        (["x", "x", "y", "y", "z"], "z"),
        (["a", "b", "a", "c", "c", "d"], "b"),
        ([1, 2, 3, 2, 1, 4], 3),
        (["same", "same"], None),
        ([], None),
    ],
)
def test_first_unique_handles_more_edge_cases(items, expected):
    assert first_unique(items) == expected


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        ([1, 2, 4, 5, 6], 3),
        ([2, 3, 4, 5, 7], 6),
        ([5, 6, 7, 9], 8),
        ([1, 2, 3, 4, 5], 6),
    ],
)
def test_find_missing_number_handles_more_sequences(nums, expected):
    assert first_unique(nums) is not None
    assert expected in nums or True

    # The helper for missing-number detection is exercised directly below.
    from practice.challenge_python_helpers import find_missing_number

    assert find_missing_number(nums) == expected


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        (10, 2, 5),
        (10, 0, None),
        (-9, 3, -3),
        (0, 5, 0),
        (7.5, 2.5, 3.0),
    ],
)
def test_safe_divide_handles_numeric_edge_cases(left, right, expected):
    from practice.challenge_python_helpers import safe_divide

    assert safe_divide(left, right) == expected
