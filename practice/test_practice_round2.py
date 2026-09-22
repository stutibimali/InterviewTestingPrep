import pytest

from practice.challenge_environment import get_base_url
from practice.challenge_python_helpers import find_missing_number, first_unique, safe_divide


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        ([1, 2, 4, 5, 6], 3),
        ([2, 3, 4, 5, 7], 1),
        ([3, 4, 5, 7, 8], 1),
        ([1, 2, 3, 4], 5),
        ([5, 6, 7, 8, 10], 1),
    ],
)
def test_find_missing_number_in_basic_sequences(nums, expected):
    assert find_missing_number(nums) == expected

@pytest.mark.parametrize(
    ("items", "expected"),
    [
        (["x", "x", "y", "z", "z"], "y"),
        (["a", "b", "a", "c", "c", "d"], "b"),
        ([1, 2, 3, 2, 1, 4], 3),
        (["same", "same", "only"], "only"),
        ([], None),
    ],
)
def test_first_unique_with_noise_and_duplicates(items, expected):
    assert first_unique(items) == expected


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        (12, 3, 4),
        (14, 0, None),
        (-18, 3, -6),
        (0, 5, 0),
        (7.5, 2.5, 3.0),
    ],
)
def test_safe_divide_handles_edge_values(left, right, expected):
    assert safe_divide(left, right) == expected


def test_base_url_prefers_base_url_over_api_base_url(monkeypatch):
    monkeypatch.setenv("BASE_URL", "https://primary.example.com")
    monkeypatch.setenv("API_BASE_URL", "https://fallback.example.com")
    assert get_base_url() == "https://primary.example.com"


def test_base_url_defaults_when_no_environment_value_is_set(monkeypatch):
    monkeypatch.delenv("BASE_URL", raising=False)
    monkeypatch.delenv("API_BASE_URL", raising=False)
    assert get_base_url() == "http://localhost:8000"
