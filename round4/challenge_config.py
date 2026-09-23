import json
import os


def read_service_config() -> dict:
    """Read SERVICE_CONFIG as a JSON object, or return an empty object."""
    raw_config = os.getenv("SERVICE_CONFIG", "{}")
    return json.loads(raw_config) if raw_config else {}