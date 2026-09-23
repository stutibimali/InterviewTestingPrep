def index_by_code(records: list[dict]) -> dict[str, dict]:
    """Index records by code, keeping the last record for duplicate codes."""
    indexed = {}
    for record in records:
        indexed.setdefault(record["code"], record)
    return indexed


def ordered_unique(values: list[str]) -> list[str]:
    """Remove duplicates without changing first-seen order."""
    return list(set(values))