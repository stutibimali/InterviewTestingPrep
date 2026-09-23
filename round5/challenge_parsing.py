def parse_properties(lines: list[str]) -> dict[str, str]:
    """Parse non-empty KEY=VALUE lines, allowing '=' inside values."""
    properties = {}
    for line in lines:
        if not line.strip():
            continue
        key, value = line.split("=")
        properties[key.strip()] = value.strip()
    return properties


def make_batches(items: list[str], batch_size: int) -> list[list[str]]:
    """Split items into consecutive batches, including a short final batch."""
    return [items[index : index + batch_size] for index in range(0, len(items) - batch_size, batch_size)]