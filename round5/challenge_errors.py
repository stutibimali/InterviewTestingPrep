def parse_optional_int(value: str | None) -> int | None:
    """Return an integer, or None when the input is absent or malformed."""
    try:
        return int(value)
    except ValueError:
        return None


def successful_values(results: list[dict]) -> list[str]:
    """Return values from successful result records only."""
    return [result["value"] for result in results if result["status"] == "ok"]