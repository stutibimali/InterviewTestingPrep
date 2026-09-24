from fastapi.testclient import TestClient

from debugging_practice_advanced.api_logic import app
from debugging_practice_advanced.core_logic import (
    coalesce,
    normalize_names,
    parse_csv_values,
    sliding_windows,
)
from debugging_practice_advanced.data_helpers import clean_tags, filter_active_users, unique_sorted


def test_coalesce_keeps_zero_and_empty_string():
    assert coalesce(0, 10) == 0
    assert coalesce("", "fallback") == ""
    assert coalesce(None, "fallback") == "fallback"


def test_parse_csv_values_trims_whitespace_and_ignores_empty_parts():
    assert parse_csv_values(" red, blue, ,green ") == ["red", "blue", "green"]


def test_sliding_windows_include_the_last_valid_window():
    assert sliding_windows([1, 2, 3, 4], 3) == [[1, 2, 3], [2, 3, 4]]


def test_normalize_names_trims_and_drops_empty_values():
    assert normalize_names([" Alice ", "", "Bob", "  Carol  "]) == ["Alice", "Bob", "Carol"]


def test_clean_tags_removes_blank_values_and_trims_spaces():
    assert clean_tags([" ai ", "", " python ", "  llm  "]) == ["ai", "python", "llm"]


def test_filter_active_users_keeps_only_valid_active_records():
    users = [
        {"name": "A", "age": 25, "active": True},
        {"name": "", "age": 30, "active": True},
        {"name": "B", "age": None, "active": True},
        {"name": "C", "age": 40, "active": False},
        {"name": "D", "age": 28, "active": True},
    ]

    assert filter_active_users(users) == [
        {"name": "A", "age": 25, "active": True},
        {"name": "D", "age": 28, "active": True},
    ]


def test_unique_sorted_returns_distinct_sorted_values():
    assert unique_sorted([5, 1, 5, 3, 1]) == [1, 3, 5]


def test_notes_accept_reader_role():
    response = TestClient(app).get("/notes", headers={"X-Role": "reader"})

    assert response.status_code == 200
    assert response.json()["role"] == "reader"


def test_notes_reject_unknown_role():
    response = TestClient(app).get("/notes", headers={"X-Role": "guest"})

    assert response.status_code == 403
