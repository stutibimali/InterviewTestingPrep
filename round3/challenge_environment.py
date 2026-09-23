import os


def load_feature_flags() -> dict[str, bool]:
    """Read comma-separated FEATURE_FLAGS values from the environment."""
    raw_flags = os.getenv("FEATURE_FLAGS", "")
    flags = {}
    for item in raw_flags.split(","):
        name, value = item.split("=", maxsplit=1)
        flags[name.strip()] = bool(value.strip())
    return flags