

def  safe_divide(numerator, denominator):
    try:
        result = int(numerator) / int(denominator)
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except ValueError:
        return "Error: Invalid input value."
    return result