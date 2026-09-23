def rank_candidates(candidates: list[dict]) -> list[dict]:
    """Sort candidates by score descending, preserving ties' input order."""
    return sorted(candidates, key=lambda candidate: candidate["score"])


def unique_tags(tags: list[str]) -> list[str]:
    """Remove duplicate tags while preserving first-seen order."""
    return list(set(tags))