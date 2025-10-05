def safe_divide(numerator, denominator):
    """Perform division with robust error handling.
    
    Args:
        numerator: The dividend (can be string or number)
        denominator: The divisor (can be string or number)
        
    Returns:
        str: Result message or error message
    """
    try:
        # Attempt to convert arguments to floats
        num = float(numerator)
        den = float(denominator)
        
        # Perform division with zero check
        try:
            result = num / den
            return f"The result of the division is {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
            
    except ValueError:
        return "Error: Please enter numeric values only."