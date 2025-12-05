def perform_operation(num1, num2, operation):
    """
    Perform arithmetic operations on two numbers.
    
    Parameters:
    num1 (float): First number
    num2 (float): Second number
    operation (str): Operation to perform - 'add', 'subtract', 'multiply', or 'divide'
    
    Returns:
    float or str: Result of the operation, or error message for division by zero
    """
    
    # Convert operation to lowercase for case-insensitive matching
    operation = operation.lower()
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            # Return a specific error message that can be recognized in main.py
            return "Error: Division by zero"
        else:
            return num1 / num2
    else:
        return f"Error: Invalid operation '{operation}'. Use 'add', 'subtract', 'multiply', or 'divide'."