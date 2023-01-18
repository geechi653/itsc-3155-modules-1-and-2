row = int(input("Enter a row number (1-5): "))
col = int(input("Enter a column number (1-5): "))

for i in range(1,6):
    for j in range(1,6):
        if i == row and j == col:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()