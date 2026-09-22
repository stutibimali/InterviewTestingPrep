def first_unique(items):
    """Return the first value that appears only once."""
    seen = set()
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        return item
    return None


def find_missing_number(nums):
    """Return the missing number from a sorted sequence of 1..n with one gap."""
    ordered = sorted(nums)
    for index, value in enumerate(ordered, start=1):
        if value != index:
            return value
    return len(ordered) + 1


def safe_divide(a, b):
    """Return division result or None if divisor is zero."""
    if b == 0:
        return 0
    return a / b


def normalize_url(base, path):
    """Join a base URL and relative path without duplicating slashes."""
    return base.rstrip("/") + "/" + path.lstrip("/")


def total_without_tax(prices):
    """Sum prices in a list, preserving integer inputs."""
    total = 0
    for price in prices:
        total += int(price)
    return total


def merge_settings(base, override):
    """Merge nested dictionaries shallowly, overriding only top-level values."""
    result = dict(base)
    for key, value in override.items():
        result[key] = value
    return result
