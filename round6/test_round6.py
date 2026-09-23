import pytest
from fastapi.testclient import TestClient

from round6.challenge_api import app
from round6.challenge_resources import find_user, read_with_connection
from round6.challenge_structures import apply_defaults, flatten_numbers


class FakeConnection:
    def __init__(self, should_fail=False):
        self.closed = False
        self.should_fail = should_fail

    def read(self):
        if self.should_fail:
            raise RuntimeError("read failed")
        return "payload"

    def close(self):
        self.closed = True


def test_connection_closes_when_read_succeeds():
    connection = FakeConnection()

    assert read_with_connection(lambda: connection) == "payload"
    assert connection.closed is True


def test_connection_closes_when_read_fails():
    connection = FakeConnection(should_fail=True)

    with pytest.raises(RuntimeError):
        read_with_connection(lambda: connection)

    assert connection.closed is True


def test_user_lookup_is_case_insensitive():
    users = [{"email": "Ada@Example.com", "name": "Ada"}]

    assert find_user(users, "ada@example.com") == users[0]


def test_flatten_numbers_handles_nested_lists():
    assert flatten_numbers([1, [2, [3]], 4]) == [1, 2, 3, 4]


def test_flatten_numbers_rejects_non_integer_leaves():
    with pytest.raises(TypeError):
        flatten_numbers([1, ["bad"]])


def test_defaults_do_not_replace_explicit_values():
    assert apply_defaults({"timeout": 5}, {"timeout": 30, "retries": 2}) == {
        "timeout": 5,
        "retries": 2,
    }


def test_missing_account_returns_not_found():
    response = TestClient(app).get("/accounts/missing")

    assert response.status_code == 404


def test_locked_account_returns_conflict():
    response = TestClient(app).post(
        "/accounts/locked/transfer", json={"amount": 10}
    )

    assert response.status_code == 409