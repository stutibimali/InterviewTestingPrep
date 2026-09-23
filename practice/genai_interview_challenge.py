"""Harder GenAI / RAG-style debugging challenge.

This file contains intentionally broken helpers that mimic common GenAI
retrieval and prompt-building problems.
"""


def chunk_text(text: str, chunk_size: int, overlap: int = 0) -> list[str]:
    """Split a text into word chunks while preserving the final remainder."""
    words = text.split()
    if chunk_size <= 0:
        return []
    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be between 0 and chunk_size")

    return [
        " ".join(words[index : index + chunk_size])
        for index in range(len(words) - chunk_size + 1)
    ]


def build_prompt(question: str, context: list[str]) -> str:
    """Build a grounded prompt from a question and supporting context."""
    cleaned_question = question.strip()
    if not cleaned_question:
        raise ValueError("question is required")

    cleaned_context = [item.strip() for item in context if item and item.strip()]
    if not cleaned_context:
        return f"Question: {cleaned_question}"

    return "\n".join([f"Question: {cleaned_question}", *cleaned_context])


def rank_documents(query: str, documents: list[str]) -> list[str]:
    """Return documents ordered by keyword overlap with the query."""
    lowered_query = query.lower().split()
    ranked = []

    for doc in documents:
        score = sum(word in doc.lower().split() for word in lowered_query)
        ranked.append((doc, score))

    ranked.sort(key=lambda item: item[1], reverse=True)
    return [doc for doc, _ in ranked]
