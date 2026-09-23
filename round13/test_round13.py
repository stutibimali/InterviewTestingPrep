from fastapi.testclient import TestClient

from round13.challenge_api import app
from round13.challenge_csv import normalize_headers, parse_row
from round13.challenge_ranking import percentile, top_k


def test_csv_parser_keeps_commas_inside_quoted_fields():
    assert parse_row('"Doe, Jane",42') == ["Doe, Jane", "42"]


def test_header_normalization_strips_outer_whitespace():
    assert normalize_headers([" First Name ", "AGE"]) == ["first_name", "age"]


def test_top_k_returns_highest_scores():
    items = [{"id": "a", "score": 8}, {"id": "b", "score": 3}, {"id": "c", "score": 9}]

    assert [item["id"] for item in top_k(items, 2)] == ["c", "a"]


def test_percentile_uses_the_last_valid_index():
    assert percentile([10, 20, 30, 40], 1.0) == 40


def test_health_returns_a_structured_response():
    response = TestClient(app).get("/health")

    assert response.json() == {"status": "ok"}


def test_metric_creation_returns_created_status():
    response = TestClient(app).post("/metrics", json={"name": "latency", "value": 12.5})

    assert response.status_code == 201