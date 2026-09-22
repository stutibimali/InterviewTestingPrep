import pytest

from practice.challenge_python_helpers import find_missing_number, first_unique, safe_divide


@pytest.mark.parametrize(
    ("items", "expected"),
    [
        (["a", "b", "a", "c", "c", "d"], "b"),
        ([1, 2, 3, 2, 1, 4], 3),
        (["x", "x", "y", "z", "z"], "y"),
        (["same", "same", "only"], "only"),
    ],
)
def test_first_unique_returns_first_non_duplicate(items, expected):
    assert first_unique(items) == expected


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        ([1, 2, 4, 5, 6], 3),
        #([2, 3, 4, 5, 7], 1),
        ([2, 3, 4, 5, 7], 6),
        ([5, 6, 7, 8, 10], 9),
        ([1, 2, 3, 4], 5),
    ],
)
def test_find_missing_number_in_middle_and_end_ranges(nums, expected):
    assert find_missing_number(nums) == expected


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        (10, 2, 5),
        (9, 3, 3),
        (-12, 3, -4),
        (7.5, 2.5, 3.0),
    ],
)
def test_safe_divide_returns_expected_result_for_valid_values(left, right, expected):
    assert safe_divide(left, right) == expected


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        (10, 0, None),
        (0, 0, None),
        (-5, 0, None),
    ],
)
def test_safe_divide_returns_none_for_zero_divisor(left, right, expected):
    assert safe_divide(left, right) == expected


@pytest.mark.parametrize(
    ("items", "expected"),
    [
        (["a", "a"], None),
        ([1, 1, 1], None),
        (["n", "n", "m"], "m"),
    ],
)
def test_first_unique_handles_all_duplicate_and_singleton_cases(items, expected):
    assert first_unique(items) == expected
