number = int(input("Enter a number to see its multiplication table:"))
multiple = 0
for iter in [1,2,3,4,5,6,7,8,9,10]:
   multiple = iter * number
   print(f"{number} * {iter} = {multiple} ")