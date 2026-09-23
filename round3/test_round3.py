from datetime import datetime, timedelta, timezone

from fastapi.testclient import TestClient

from round3.challenge_api import app
from round3.challenge_collections import group_shipments_by_region, summarize_scores
from round3.challenge_environment import load_feature_flags
from round3.challenge_time import build_retry_delays, expires_at


def test_feature_flags_parse_false_and_true_values(monkeypatch):
    monkeypatch.setenv("FEATURE_FLAGS", "dark_mode=false, audit_log=true")

    assert load_feature_flags() == {"dark_mode": False, "audit_log": True}


def test_shipments_are_grouped_under_each_region():
    shipments = [
        {"id": "a1", "region": "east"},
        {"id": "b2", "region": "west"},
        {"id": "c3", "region": "east"},
    ]

    assert group_shipments_by_region(shipments) == {
        "east": [shipments[0], shipments[2]],
        "west": [shipments[1]],
    }


def test_score_summary_keeps_fractional_mean():
    assert summarize_scores([2, 3]) == {
        "count": 2,
        "minimum": 2,
        "maximum": 3,
        "mean": 2.5,
    }


def test_dispatch_response_keeps_packages_numeric():
    client = TestClient(app)

    response = client.post(
        "/dispatches",
        json={"tracking_code": "ZX-1234", "destination": "LHR", "packages": 3},
    )

    assert response.status_code == 201
    assert response.json()["packages"] == 3


def test_dispatch_validation_rejects_short_tracking_code():
    response = TestClient(app).post(
        "/dispatches",
        json={"tracking_code": "short", "destination": "LHR", "packages": 1},
    )

    assert response.status_code == 422


def test_expiration_does_not_shift_an_aware_timestamp():
    created = datetime(2026, 9, 22, 10, 0, tzinfo=timezone(timedelta(hours=5)))

    assert expires_at(created, 30) == datetime(
        2026, 9, 22, 5, 30, tzinfo=timezone.utc
    )


def test_retry_delays_do_not_leak_between_calls():
    assert build_retry_delays(2) == [1, 2]
    assert build_retry_delays(1) == [1]