from datetime import datetime

from fastapi.testclient import TestClient
from pydantic import ValidationError
import pytest

from final_assessment_part3.challenge_api import Schedule, app
from final_assessment_part3.challenge_core import (
    normalize_status,
    project_fields,
    retry_delays,
)


def test_status_normalization_trims_and_lowercases():
    assert normalize_status("  READY ") == "ready"


def test_retry_delays_have_exact_attempt_count_and_cap():
    assert retry_delays(3, 4) == [1, 2, 4]


def test_field_projection_does_not_mutate_source():
    record = {"id": 1, "name": "Ada", "secret": "hidden"}

    assert project_fields(record, ["id", "name"]) == {"id": 1, "name": "Ada"}
    assert record == {"id": 1, "name": "Ada", "secret": "hidden"}


def test_schedule_requires_end_after_start():
    with pytest.raises(ValidationError):
        Schedule(
            starts_at=datetime(2026, 9, 23, 12),
            ends_at=datetime(2026, 9, 23, 11),
        )


def test_job_run_returns_accepted_status():
    response = TestClient(app).post("/jobs/job-1/run", json={})

    assert response.status_code == 202


def test_missing_job_run_returns_not_found():
    response = TestClient(app).post("/jobs/missing/run", json={})

    assert response.status_code == 404


def test_events_reject_limit_above_maximum():
    response = TestClient(app).get("/events?limit=101")

    assert response.status_code == 422