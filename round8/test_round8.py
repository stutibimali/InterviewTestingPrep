from fastapi.testclient import TestClient

from round8.challenge_api import app
from round8.challenge_records import index_by_code, ordered_unique
from round8.challenge_values import clamp, mean_or_none


def test_clamp_applies_both_bounds():
    assert clamp(15, 0, 10) == 10
    assert clamp(-2, 0, 10) == 0


def test_mean_of_empty_values_is_none():
    assert mean_or_none([]) is None


def test_duplicate_record_code_keeps_the_last_record():
    records = [
        {"code": "A", "version": 1},
        {"code": "A", "version": 2},
    ]

    assert index_by_code(records) == {"A": records[1]}


def test_ordered_unique_preserves_first_seen_order():
    assert ordered_unique(["b", "a", "b", "c"]) == ["b", "a", "c"]


def test_mismatched_task_ids_return_bad_request():
    response = TestClient(app).put(
        "/tasks/path-id",
        json={"task_id": "body-id", "completed": True},
    )

    assert response.status_code == 400


def test_protected_task_delete_is_not_allowed():
    response = TestClient(app).delete("/tasks/protected")

    assert response.status_code == 405