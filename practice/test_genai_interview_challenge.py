from practice.genai_interview_challenge import build_prompt, chunk_text, rank_documents


def test_chunk_text_keeps_final_remainder_and_full_chunks():
    assert chunk_text("one two three four five six", 3) == [
        "one two three",
        "four five six",
    ]


def test_build_prompt_formats_question_and_context_cleanly():
    question = " What is the refund policy? "
    context = ["Refunds are processed within 5 business days.", " " ]

    assert build_prompt(question, context) == (
        "Question: What is the refund policy?\n"
        "Refunds are processed within 5 business days."
    )


def test_rank_documents_prioritizes_relevant_matches():
    docs = [
        "The billing policy explains refund timing.",
        "Weather in Tokyo is mild this week.",
        "User profile settings are under account controls.",
    ]

    assert rank_documents("refund timing", docs) == [
        "The billing policy explains refund timing.",
        "User profile settings are under account controls.",
        "Weather in Tokyo is mild this week.",
    ]
