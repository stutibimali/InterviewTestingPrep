"""Data normalization and filtering helper functions."""


def clean_tags(tags: list[str]) -> list[str]:
    """Trim whitespace, remove empty tags, and preserve order."""
    cleaned = []
    for tag in tags:
        value = tag.strip()
        if value:
            cleaned.append(value)
    return cleaned


def filter_active_users(users: list[dict]) -> list[dict]:
    """Return only active users with a valid name and age."""
    return [
        user
        for user in users
        if user.get("active") is True and user.get("name") and user.get("age") is not None
    ]


def unique_sorted(values: list[int]) -> list[int]:
    """Return distinct values sorted in ascending order."""
    return sorted(set(values))
