from datetime import datetime

from fastapi.testclient import TestClient

from round14.challenge_api import app
from round14.challenge_dates import deduplicate, parse_date
from round14.challenge_numbers import is_slug, total_price


def test_total_price_rounds_the_final_amount():
    assert total_price([0.1, 0.2], 0.1) == 0.33


def test_slug_requires_every_character_to_be_allowed():
    assert is_slug("valid-slug-2") is True
    assert is_slug("bad slug!") is False


def test_parse_date_uses_iso_calendar_order():
    assert parse_date("2026-09-23") == datetime(2026, 9, 23)


def test_deduplicate_preserves_first_seen_order():
    assert deduplicate(["a", "b", "a", "c"]) == ["a", "b", "c"]


def test_preferences_coerce_query_values():
    response = TestClient(app).get("/preferences?page=3&compact=true")

    assert response.json() == {"page": 3, "compact": True}


def test_preferences_reject_page_zero():
    response = TestClient(app).get("/preferences?page=0")

    assert response.status_code == 422