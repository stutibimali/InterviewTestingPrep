from fastapi.testclient import TestClient

from round10.challenge_api import app
from round10.challenge_inputs import normalize_tags, parse_range
from round10.challenge_merge import merge_counts
from round10.challenge_retry import backoff_seconds, should_retry


def test_normalize_tags_accepts_a_single_string_as_one_tag():
    assert normalize_tags(" Python ") == ["python"]


def test_normalize_tags_normalizes_a_list():
    assert normalize_tags([" API ", "FastAPI"]) == ["api", "fastapi"]


def test_parse_range_supports_negative_start_values():
    assert parse_range("-3:4") == (-3, 4)


def test_retryable_statuses_are_server_errors_not_client_errors():
    assert should_retry(429) is False
    assert should_retry(500) is True
    assert should_retry(503) is True


def test_first_backoff_attempt_starts_at_base():
    assert backoff_seconds(0) == 0.5


def test_merge_counts_adds_overlapping_keys():
    assert merge_counts({"ok": 2, "failed": 1}, {"ok": 3}) == {
        "ok": 5,
        "failed": 1,
    }


def test_search_requires_a_meaningful_query():
    response = TestClient(app).get("/search?q=x")

    assert response.status_code == 422