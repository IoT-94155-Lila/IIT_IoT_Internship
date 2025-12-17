import math

def area_circle(radius):
    """
    Calculate the area of a circle.
    
    Formula: π * r^2
    
    Parameters:
        radius (float or int): Radius of the circle. Must be non-negative.
    
    Returns:
        float: Area of the circle.
    
    Raises:
        ValueError: If radius is negative or not a number.
    """
    if not isinstance(radius, (int, float)):
        raise ValueError("Radius must be a number.")
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * (radius ** 2)


def area_rectangle(length, width):
    """
    Calculate the area of a rectangle.
    
    Formula: length * width
    
    Parameters:
        length (float or int): Length of the rectangle. Must be non-negative.
        width (float or int): Width of the rectangle. Must be non-negative.
    
    Returns:
        float: Area of the rectangle.
    
    Raises:
        ValueError: If length or width is negative or not a number.
    """
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise ValueError("Length and width must be numbers.")
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative.")
    return length * width

