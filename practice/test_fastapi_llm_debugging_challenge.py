from fastapi.testclient import TestClient

from practice.fastapi_llm_debugging_challenge import app


def test_chat_rejects_blank_question():
    response = TestClient(app).post("/chat", json={"question": "   ", "context": ["Alpha"]})

    assert response.status_code == 400
    assert response.json()["detail"] == "question is required"


def test_chat_deduplicates_and_ignores_empty_context_entries():
    response = TestClient(app).post(
        "/chat",
        json={
            "question": "What is the refund policy?",
            "context": ["Refunds take 5 days.", " ", "Refunds take 5 days.", "Billing policy"],
        },
    )

    assert response.status_code == 200
    assert "Refunds take 5 days." in response.json()["answer"]
    assert "Billing policy" in response.json()["answer"]


def test_chat_requires_context_for_knowledgeable_answer():
    response = TestClient(app).post("/chat", json={"question": "What is the refund policy?", "context": []})

    assert response.status_code == 200
    assert "need more context" in response.json()["answer"].lower()
