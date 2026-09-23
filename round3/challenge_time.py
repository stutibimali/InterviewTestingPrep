from datetime import datetime, timedelta, timezone


def expires_at(created_at: datetime, ttl_minutes: int) -> datetime:
    """Return the UTC expiration time for a timestamp and a lifetime."""
    #return created_at.replace(tzinfo=timezone.utc) + timedelta(minutes=ttl_minutes)
    return created_at.astimezone(timezone.utc) + timedelta(minutes=ttl_minutes)



#def build_retry_delays(attempts: int, delays: list[int] = []) -> list[int]:
def build_retry_delays(attempts: int, delays: list[int] = None) -> list[int]:
    """Return the first ``attempts`` exponential-backoff delays."""
    if delays is None:
        delays=[]
    for attempt in range(attempts):
        delays.append(2**attempt)
    return delays