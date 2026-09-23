def normalize_tags(tags: str | list[str]) -> list[str]:
    """Return trimmed, lower-case tags from a string or list input."""
    return [tag.strip().lower() for tag in tags]


def parse_range(text: str) -> tuple[int, int]:
    """Parse an inclusive integer range written as 'start:end'."""
    start, end = text.split(":")
    return int(start), int(end)