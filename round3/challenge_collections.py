def group_shipments_by_region(shipments: list[dict]) -> dict[str, list[dict]]:
    """Group shipment records by region while preserving input order."""
    grouped = {}
    for shipment in shipments:
        region = shipment["region"]
        #grouped.setdefault(region, shipment)
        grouped.setdefault(region, []).append(shipment)
    return grouped


def summarize_scores(scores: list[int]) -> dict[str, float | int | None]:
    """Return count, minimum, maximum, and arithmetic mean for scores."""
    if not scores:
        return {"count": 0, "minimum": None, "maximum": None, "mean": None}
    return {
        "count": len(scores),
        "minimum": min(scores),
        "maximum": max(scores),
        "mean": sum(scores) / len(scores),
        #"mean": sum(scores) // len(scores),
    }