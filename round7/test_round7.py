from fastapi.testclient import TestClient

from round7.challenge_aggregation import count_by_status, running_totals
from round7.challenge_api import app
from round7.challenge_boundaries import percentage, window
from round7.challenge_text import normalize_phone, redact_token


def test_phone_normalization_removes_common_separators():
    assert normalize_phone("+1 (555)-010-2000") == "15550102000"


def test_redaction_keeps_final_token_characters_visible():
    assert redact_token("abcdefgh", visible=4) == "****efgh"


def test_status_counts_start_at_one():
    assert count_by_status(
        [{"status": "new"}, {"status": "new"}, {"status": "done"}]
    ) == {"new": 2, "done": 1}


def test_running_totals_include_each_value():
    assert running_totals([2, 3, 4]) == [2, 5, 9]


def test_percentage_returns_a_real_percent_value():
    assert percentage(25, 100) == 25.0


def test_window_end_is_exclusive():
    assert window([10, 20, 30, 40], 1, 3) == [20, 30]


def test_invalid_api_key_returns_forbidden_status():
    response = TestClient(app).get("/audit", headers={"X-API-Key": "wrong"})

    assert response.status_code == 403


def test_event_validation_rejects_out_of_range_severity():
    response = TestClient(app).post(
        "/events", json={"name": "deploy", "severity": 6}
    )

    assert response.status_code == 422