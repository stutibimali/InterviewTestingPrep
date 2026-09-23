def normalize_status(value: str) -> str:
    """Normalize a status label for comparisons."""
    return value.lower().strip()


def retry_delays(attempts: int, maximum: int) -> list[int]:
    """Return capped exponential delays starting at one second."""
    return [min(2**attempt, maximum) for attempt in range(attempts)]


def project_fields(record: dict, fields: list[str]) -> dict:
    """Return a selected-field copy without changing the source record."""
    return {key: record[key] for key in fields if key in record}
    """projected = record
    for key in list(projected):
        if key not in fields:
            del projected[key]
    return projected"""