def normalize_status(value: str) -> str:
    """Normalize a status label for comparisons."""
    return value.lower()


def retry_delays(attempts: int, maximum: int) -> list[int]:
    """Return capped exponential delays starting at one second."""
    return [min(2**attempt, maximum) for attempt in range(attempts + 1)]


def project_fields(record: dict, fields: list[str]) -> dict:
    """Return a selected-field copy without changing the source record."""
    projected = record
    for key in list(projected):
        if key not in fields:
            del projected[key]
    return projected