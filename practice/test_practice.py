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
