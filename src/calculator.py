def add(first_number: int, second_number: int):
    """Return the sum of two numbers."""
    return first_number + second_number


def substract(first_number: int, second_number: int):
    """Return the difference of two numbers."""
    return first_number - second_number


def multiply(first_number: int, second_number: int):
    """Return the product of two numbers."""
    return first_number * second_number


def divide(first_number: int, second_number: int):
    """Return the quotient of two numbers."""
    if second_number == 0:
        raise ValueError("Cannot divide by zero.")

    return first_number / second_number
