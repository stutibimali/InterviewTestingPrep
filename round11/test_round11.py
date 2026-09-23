from datetime import datetime

from fastapi.testclient import TestClient

from round11.challenge_api import app
from round11.challenge_json import encode_record
from round11.challenge_mapping import first_present, invert_mapping
from round11.challenge_shapes import ensure_same_length, transpose


def test_transpose_preserves_matrix_columns():
    assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]


def test_same_length_returns_true_only_for_equal_lengths():
    assert ensure_same_length([1, 2], [3, 4]) is True
    assert ensure_same_length([1], [2, 3]) is False


def test_inverted_mapping_normalizes_both_sides():
    assert invert_mapping({"A": "One", "B": "Two"}) == {
        "one": "a",
        "two": "b",
    }


def test_first_present_keeps_zero_as_a_real_value():
    assert first_present({"count": 0, "fallback": 4}, ["count", "fallback"]) == 0


def test_encode_record_sorts_keys_for_deterministic_output():
    assert encode_record({"b": 2, "a": 1}) == '{"a": 1, "b": 2}'


def test_missing_message_returns_not_found():
    response = TestClient(app).get("/messages/missing")

    assert response.status_code == 404


def test_blank_message_returns_bad_request():
    response = TestClient(app).post("/messages", params={"text": "   "})

    assert response.status_code == 400