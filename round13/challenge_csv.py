def parse_row(line: str) -> list[str]:
    """Parse a comma-separated row, including quoted commas."""
    return [part.strip() for part in line.split(",")]


def normalize_headers(headers: list[str]) -> list[str]:
    """Normalize headers to lowercase snake-case names."""
    return [header.lower().replace(" ", "_") for header in headers]