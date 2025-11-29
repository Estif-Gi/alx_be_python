size = int(input("Enter the size of the pattern:"))
row = 0
while row < size:
    for i in range(1,size):
        print("*",end="")
        print("")
    row +=1