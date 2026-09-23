def parse_bool(value: str) -> bool:
    """Parse common true and false text values."""
    return value.strip().lower() == "true"


def format_duration(total_seconds: int) -> str:
    """Format seconds as MM:SS."""
    minutes, seconds = divmod(total_seconds, 60)
    return f"{minutes:02d}:{total_seconds:02d}"