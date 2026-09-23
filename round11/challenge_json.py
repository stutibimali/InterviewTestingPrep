import json


def encode_record(record: dict) -> str:
    """Encode a record deterministically for logs and snapshots."""
    return json.dumps(record)