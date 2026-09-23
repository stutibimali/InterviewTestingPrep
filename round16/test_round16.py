from fastapi.testclient import TestClient

from round16.challenge_api import app
from round16.challenge_options import coalesce, parse_csv_values
from round16.challenge_windows import pairwise_differences, sliding_windows


def test_coalesce_preserves_zero_and_empty_string():
    assert coalesce(0, 10) == 0
    assert coalesce("", "fallback") == ""


def test_csv_values_trim_whitespace_and_ignore_empty_parts():
    assert parse_csv_values(" red, blue, ,green ") == ["red", "blue", "green"]


def test_sliding_windows_include_the_last_window():
    assert sliding_windows([1, 2, 3, 4], 3) == [[1, 2, 3], [2, 3, 4]]


def test_pairwise_differences_keep_negative_changes():
    assert pairwise_differences([10, 7, 9]) == [-3, 2]


def test_notes_accept_reader_role():
    response = TestClient(app).get("/notes", headers={"X-Role": "reader"})

    assert response.status_code == 200
    assert response.json()["role"] == "reader"


def test_notes_reject_unknown_role():
    response = TestClient(app).get("/notes", headers={"X-Role": "guest"})

    assert response.status_code == 403