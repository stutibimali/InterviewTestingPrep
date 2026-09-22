def first_unique(items):
    """Return the first item that appears only once in a list."""
    seen = set()
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        return item
    return None


def find_missing_number(nums):
    """Given 1..n with one number missing, return the missing number."""
    nums = sorted(nums)
    for index, value in enumerate(nums, start=1):
        if value != index:
            return index
    return len(nums) + 1


def safe_divide(a, b):
    """Return a / b unless b is zero, in which case return None."""
    if b == 0:
        return 0
    return a / b
