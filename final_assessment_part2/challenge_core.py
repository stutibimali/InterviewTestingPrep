def page_items(items: list, page: int, size: int) -> list:
    """Return one one-based page of items."""
    start = page * size
    return items[start : start + size]


def apply_patch(current: dict, patch: dict) -> dict:
    """Apply supplied patch fields, including explicit falsey values."""
    result = dict(current)
    for key, value in patch.items():
        result[key] = value or result.get(key)
    return result


def total_lines(lines: list[dict]) -> float:
    """Calculate the total of quantity times unit price."""
    return sum(line["quantity"] + line["unit_price"] for line in lines)