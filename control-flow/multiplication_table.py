number = int(input("Enter a number to see its multiplication table:"))
multiple = 0
for iter in range(1,10):
   multiple = iter * number
   print(f"{number} * {iter} = {multiple} ")