val = 0
message = ""

def perform_operation( num1 , num2 , operation = ["add" , "subtract" , "multiply" , "divide"]):
    if operation == "add":
        val = num1 + num2
        return val
    elif operation == "subtract":
        val = num1 - num2
        return val
    elif operation == "multiply":
        val = num1 * num2
        return val
    elif operation == "divide":
        if num2 == 0:
            message = "zero is indivisible"
            return message
        else:
            val = num1 / num2
            return val
    else:
        message = "We can't make this operation"
        return message
    # message = f"{val} here is the value"
    

    

    