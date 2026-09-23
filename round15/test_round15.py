from fastapi.testclient import TestClient

from round15.challenge_api import app
from round15.challenge_state import append_event, cache_value
from round15.challenge_validation import is_identifier, validate_required_fields


def test_identifier_requires_the_whole_string_to_match():
    assert is_identifier("valid_123") is True
    assert is_identifier("valid-123") is False
    assert is_identifier("valid-123!") is False


def test_required_field_check_reports_empty_values_when_required():
    assert validate_required_fields({"name": "Ada", "email": ""}, ["name", "email"]) == []


def test_cache_keeps_values_separate_by_namespace():
    cache = {}

    assert cache_value(cache, "users", "1", lambda: "Ada") == "Ada"
    assert cache_value(cache, "orders", "1", lambda: "Order-1") == "Order-1"


def test_append_event_does_not_mutate_input():
    original = [{"name": "start"}]

    result = append_event(original, {"name": "finish"})

    assert original == [{"name": "start"}]
    assert result == [{"name": "start"}, {"name": "finish"}]


def test_profile_response_excludes_internal_fields():
    response = TestClient(app).get("/profiles/ada")

    assert response.json() == {"username": "ada", "active": True}