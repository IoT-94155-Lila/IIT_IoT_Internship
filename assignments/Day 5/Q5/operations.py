def add(a, b):
    """Return the sum of two numbers."""
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both arguments must be int or float.")
    return a + b


def multiply(a, b):
    """Return the product of two numbers."""
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both arguments must be int or float.")
    return a * b

"""
string_ops.py
Contains basic string operations.
"""

def reverse_string(s):
    """Return the reversed version of the input string."""
    if not isinstance(s, str):
        raise TypeError("Argument must be a string.")
    return s[::-1]
