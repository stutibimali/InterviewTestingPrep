from datetime import datetime, timedelta, timezone

from fastapi.testclient import TestClient

from round12.challenge_api import app
from round12.challenge_dates import is_expired, sort_events
from round12.challenge_paths import join_url, safe_filename


def test_safe_filename_removes_parent_directories():
    assert safe_filename("../../reports/result.csv") == "result.csv"


def test_join_url_normalizes_slashes():
    assert join_url("https://api.example/", "/v1/items") == "https://api.example/v1/items"


def test_expiry_handles_a_naive_timestamp_with_explicit_now():
    now = datetime(2026, 9, 23, 12, 0, tzinfo=timezone.utc)
    expires = now - timedelta(minutes=1)

    assert is_expired(expires, now) is True


def test_events_are_sorted_by_priority():
    events = [{"name": "low", "priority": 3}, {"name": "high", "priority": 1}]

    assert [event["name"] for event in sort_events(events)] == ["high", "low"]


def test_upload_returns_created_status():
    response = TestClient(app).post("/uploads", params={"filename": "a.txt", "size": 4})

    assert response.status_code == 201


def test_upload_rejects_negative_size():
    response = TestClient(app).post("/uploads", params={"filename": "a.txt", "size": -1})

    assert response.status_code == 422