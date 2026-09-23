def split_valid_records(records):
    """Return valid records and the number of rejected records."""
    valid_records = (record for record in records if record.get("valid"))
    return list(valid_records), sum(1 for record in valid_records if not record.get("valid"))


def clone_with_label(record: dict, label: str) -> dict:
    """Copy a record and replace its nested metadata label."""
    copied = record.copy()
    copied["metadata"]["label"] = label
    return copied