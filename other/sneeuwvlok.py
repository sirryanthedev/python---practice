# (ex. sneeuwvlok - Dodona)

# keep asking for input until the correct type of input is given
while True:
    n = int(input("Enter an odd positive integer number: "))
    if n % 2 != 0:
        break
    print("Try again, that number was not odd...")

nxn = []

# add the second dimension
for row in range(n):
    nxn.append([])

# fill the 2d list with dots
for row in range(n):
    for col in range(n):
        nxn[row].append(".")

# make a vertical chain of asterisks in the middle
for row in range(n):
    nxn[row][n//2] = "*"

# make a horizontal chain of asterisks in the middle
for col in range(n):
    nxn[n//2][col] = "*"

# make a diagonal chain of asterisks (top-left -> bottom-right)
for row_col in range(n):
    nxn[row_col][row_col] = "*"

# make a diagonal chain of asterisks (bottom-left -> top-right)
for i in range(n):
    nxn[i][n - 1 - i] = "*"

# print the final contents of the 2d list
for row in nxn:
    for col in row:
        print(col, end=" ")
    print()