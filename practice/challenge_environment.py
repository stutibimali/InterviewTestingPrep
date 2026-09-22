import os


def get_base_url() -> str:
    """Return the configured base URL for the API client."""
    value = os.getenv("BASE_URL")  or os.getenv("API_BASE_URL") or os.getenv("APP_ENV") or os.getenv("ENV") or "http://localhost:8000"
    #value = os.getenv("BASE_URL") or os.getenv("API_BASE_URL") or "http://localhost:8000"
    #return value.lstrip("https://")
    return value