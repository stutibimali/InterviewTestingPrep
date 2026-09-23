from datetime import datetime

from fastapi.testclient import TestClient

from round5.challenge_api import app
from round5.challenge_errors import parse_optional_int, successful_values
from round5.challenge_parsing import make_batches, parse_properties
from round5.challenge_serialization import event_payload


def test_properties_allow_equals_inside_values():
    assert parse_properties(["mode=fast", "query=a=b=c"]) == {
        "mode": "fast",
        "query": "a=b=c",
    }


def test_batches_include_the_short_final_batch():
    assert make_batches(["a", "b", "c", "d", "e"], 2) == [
        ["a", "b"],
        ["c", "d"],
        ["e"],
    ]


def test_optional_integer_accepts_missing_values():
    assert parse_optional_int(None) is None
    assert parse_optional_int("12") == 12
    assert parse_optional_int("bad") is None


def test_successful_values_ignore_failed_records():
    results = [
        {"status": "ok", "value": "ready"},
        {"status": "failed", "value": "discard"},
    ]

    assert successful_values(results) == ["ready"]


def test_event_payload_uses_iso_datetime_format():
    occurred_at = datetime(2026, 9, 23, 14, 5, 6)

    assert event_payload("started", occurred_at) == {
        "name": "started",
        "occurred_at": "2026-09-23T14:05:06",
    }


def test_report_pagination_uses_offset_and_limit():
    response = TestClient(app).get("/reports?offset=1&limit=2")

    assert response.status_code == 200
    assert response.json() == {"items": ["weekly", "monthly"], "total": 4}


def test_patch_preserves_an_explicit_empty_string():
    response = TestClient(app).patch("/reports/r1", json={"title": ""})

    assert response.status_code == 200
    assert response.json()["title"] == ""