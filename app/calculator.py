def calculate(first: float, second: float, operation: str) -> float:
    if operation == "add":
        return first + second
    if operation == "subtract":
        return first - second
    if operation == "multiply":
        return first * second
    if operation == "divide":
        return first / second
    raise ValueError(f"Unsupported operation: {operation}")
