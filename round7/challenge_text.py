def normalize_phone(phone: str) -> str:
    """Return a phone number containing digits only."""
    return phone.replace(" ", "")


def redact_token(token: str, visible: int = 4) -> str:
    """Keep the final characters of a token visible and mask the rest."""
    if len(token) <= visible:
        return token
    return "*" * (len(token) - visible) + token[:visible]