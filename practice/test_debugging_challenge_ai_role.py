import pytest

from practice.debugging_challenge_ai_role import (
    coalesce,
    get_role,
    parse_csv_values,
    sliding_windows,
)


def test_coalesce_keeps_zero_and_empty_string():
    assert coalesce(0, 10) == 0
    assert coalesce("", "fallback") == ""
    assert coalesce(None, "fallback") == "fallback"


def test_parse_csv_values_trims_whitespace_and_ignores_empty_parts():
    assert parse_csv_values(" red, blue, ,green ") == ["red", "blue", "green"]


def test_sliding_windows_include_the_last_valid_window():
    assert sliding_windows([1, 2, 3, 4], 3) == [[1, 2, 3], [2, 3, 4]]


def test_get_role_accepts_supported_roles():
    assert get_role("reader") == "reader"
    assert get_role("editor") == "editor"


def test_get_role_rejects_unsupported_roles():
    with pytest.raises(ValueError):
        get_role("guest")
