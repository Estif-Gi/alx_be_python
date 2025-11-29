
def calculation(res):

    match res:
        case "+":
            result = num1 + num2
            return result
        case "-":
            result = num1 - num2
            return result
        case "*":
            result =  num1 * num2
            return result
        case "/":
            if num2 != 0:
              result = num1 / num2
              return result
            else:
                print("can not divide by zero")
        case _:
            print("i cant help you with this calculation")

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

res = input("Choose the operation (+, -, *, /):")

result = calculation(res)
print(f"The result is {result}")
