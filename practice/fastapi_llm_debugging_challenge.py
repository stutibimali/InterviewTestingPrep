"""FastAPI + LLM debugging challenge.

This module contains intentionally broken code for a simple chat endpoint.
"""

from fastapi import FastAPI, HTTPException

app = FastAPI(title="LLM Debug Lab")


def sanitize_context(context: list[str] | None) -> list[str]:
    """Remove blanks and duplicates but keep order."""
    if context is None:
        return []

    cleaned = []
    for item in context:
        text = str(item).strip()
        if text and text not in cleaned:
            cleaned.append(text)
    return cleaned


def build_answer(question: str, context: list[str] | None) -> str:
    """Build a grounded answer from a question and context."""
    if not question or not question.strip():
        raise ValueError("question is required")

    cleaned_context = sanitize_context(context)
    if not cleaned_context:
        return "I need more context to answer that question."

    return f"Based on the context: {" ".join(cleaned_context)} | Question: {question.strip()}"


@app.post("/chat")
def chat(payload: dict):
    """Process a chat request with optional context."""
    question = payload.get("question", "")
    context = payload.get("context", [])

    try:
        answer = build_answer(question, context)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    return {"answer": answer}
