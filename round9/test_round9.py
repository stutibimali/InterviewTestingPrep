from fastapi.testclient import TestClient

from round9.challenge_api import app
from round9.challenge_conversion import format_duration, parse_bool
from round9.challenge_lookup import get_nested, partition_even


def test_parse_bool_accepts_common_false_values():
    assert parse_bool("false") is False
    assert parse_bool("NO") is False
    assert parse_bool("0") is False


def test_parse_bool_accepts_common_true_values():
    assert parse_bool("true") is True
    assert parse_bool("YES") is True
    assert parse_bool("1") is True


def test_duration_wraps_seconds_at_sixty():
    assert format_duration(125) == "02:05"


def test_nested_lookup_returns_default_for_missing_intermediate_path():
    assert get_nested({"account": {}}, "account.preferences.theme", "light") == "light"


def test_partition_preserves_even_and_odd_order():
    assert partition_even([3, 2, 4, 1]) == ([2, 4], [3, 1])


def test_job_creation_returns_accepted_status():
    response = TestClient(app).post(
        "/jobs", json={"name": "index", "priority": 2}
    )

    assert response.status_code == 202


def test_missing_job_returns_not_found():
    response = TestClient(app).get("/jobs/missing")

    assert response.status_code == 404