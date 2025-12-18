# (ex. Wissel kolommen van 2d lijst - Dodona)

row_col = input("Enter the number of rows followed by a space, and the number of columns: ")
rows = int(row_col.split()[0])
cols = int(row_col.split()[1])

matrix = []

for row in range(rows):
    matrix.append([])
count = 0

while count < rows:
    line = input(f"Enter row number {count + 1}: ")

    matrix[count].extend(line.split())

    count += 1

while True:
    col1_col2 = input("Swap columns - enter the first column number followed by a space, and the second one: ")
    col_1 = int(col1_col2.split()[0])
    col_2 = int(col1_col2.split()[1])
    if 0 <= col_1 < cols and 0 <= col_2 < cols:
        break
    print("Enter valid numbers for the columns!")

for row in matrix:
    temp = row[col_1]
    row[col_1] = row[col_2]
    row[col_2] = temp

for row in matrix:
    for col in row:
        print(col, end=" ")
    print("\n")