class Connection:
    def __init__(self):
        self.closed = False

    def close(self):
        self.closed = True


def read_with_connection(loader):
    """Load data and always close the connection returned by loader."""
    connection = loader()
    data = connection.read()
    connection.close()
    return data


def find_user(users: list[dict], email: str) -> dict | None:
    """Find a user by email without treating letter case as significant."""
    return next((user for user in users if user["email"] == email.lower()), None)