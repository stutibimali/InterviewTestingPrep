import json

from fastapi.testclient import TestClient

from round4.challenge_api import app
from round4.challenge_config import read_service_config
from round4.challenge_iterators import clone_with_label, split_valid_records
from round4.challenge_ordering import rank_candidates, unique_tags


def test_split_valid_records_counts_rejected_records():
    records = [{"id": 1, "valid": True}, {"id": 2, "valid": False}]

    assert split_valid_records(records) == ([records[0]], 1)


def test_clone_does_not_mutate_original_nested_metadata():
    original = {"id": "x1", "metadata": {"label": "source"}}

    copied = clone_with_label(original, "copy")

    assert copied["metadata"]["label"] == "copy"
    assert original["metadata"]["label"] == "source"


def test_candidates_are_ranked_highest_score_first():
    candidates = [{"name": "A", "score": 8}, {"name": "B", "score": 3}]

    assert [candidate["name"] for candidate in rank_candidates(candidates)] == ["A", "B"]


def test_unique_tags_keep_first_seen_order():
    assert unique_tags(["red", "blue", "red", "green"]) == ["red", "blue", "green"]


def test_service_config_is_decoded_from_json(monkeypatch):
    monkeypatch.setenv("SERVICE_CONFIG", json.dumps({"region": "eu", "retries": 2}))

    assert read_service_config() == {"region": "eu", "retries": 2}


def test_inventory_query_parameters_are_read_from_query_string():
    response = TestClient(app).get("/inventory?limit=4&include_archived=true")

    assert response.status_code == 200
    assert response.json() == {"limit": 4, "include_archived": True}


def test_reservation_rejects_requests_above_available_stock():
    response = TestClient(app).post(
        "/reservations",
        json={"item_id": "sku-7", "requested": 6, "available": 4},
    )

    assert response.status_code == 422