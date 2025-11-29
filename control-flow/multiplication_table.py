number = int(input("Enter a number to see its multiplication table:"))
multiple = 0
for i in range(1,11):
   multiple = i * number
   print(f"{number} * {i} = {multiple} ")