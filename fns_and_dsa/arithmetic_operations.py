def perform_operation(num1: float, num2: float, operation: str):
   
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
            return "Error: Division by zero is not allowed."
        else:
            return num1 / num2
    else:
        return f"Error: Invalid operation '{operation}'. Use 'add', 'subtract', 'multiply', or 'divide'."