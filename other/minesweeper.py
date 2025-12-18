# (ex. Minesweeper - Dodona)

tests = int(input("Enter the number of tests: "))
count = 0
total = []
# initialise total list:
for test in range(tests):
    total.append([])

while count < tests:
    rows_cols = input("Enter the amount of rows, followed by a space and the amount of columns: ")

    rows = int(rows_cols.split()[0])
    cols = int(rows_cols.split()[1])

    converted_input = []
    # initialise converted_input list:
    for row in range(rows):
        converted_input.append([])

    for row in range(rows):
        row_str = input(f"Enter row number {row + 1}: ")
        for char in row_str:
            converted_input[row].append(char)
        
    converted_input_result = []

    # initialise converted_input_result list:
    for row in range(rows):
        converted_input_result.append([])
        for col in range(cols):
            converted_input_result[row].append(0)

    # loop through converted_input list and perform checks for "*"
    for row in range(rows):
        for col in range(cols):
            if converted_input[row][col] == "*":
                converted_input_result[row][col] = converted_input[row][col]
            else:
                # if possible: check previous column for "*"
                if col > 0:
                    if converted_input[row][col - 1] == "*":
                        converted_input_result[row][col] += 1
                # if possible: check following column for "*"
                if col < cols - 1:
                    if converted_input[row][col + 1] == "*":
                        converted_input_result[row][col] += 1
                # if possible: check following row for "*"
                if row < rows - 1:
                    if converted_input[row + 1][col] == "*":
                        converted_input_result[row][col] += 1
                # if possible: check previous row for "*"
                if row > 0:
                    if converted_input[row - 1][col] == "*":
                        converted_input_result[row][col] += 1
                # if possible: check lower-right diagonally for "*"
                if row < rows - 1 and col < cols - 1:
                    if converted_input[row + 1][col + 1] == "*":
                        converted_input_result[row][col] += 1
                # if possible: check lower-left diagonally for "*"
                if row < rows - 1 and col > 0:
                    if converted_input[row + 1][col - 1] == "*":
                        converted_input_result[row][col] += 1
                # if possible: check upper-right diagonally for "*"
                if row > 0 and col < cols - 1:
                    if converted_input[row - 1][col + 1] == "*":
                        converted_input_result[row][col] += 1
                # if possible: check upper-left diagonally for "*"
                if row > 0 and col > 0:
                    if converted_input[row - 1][col - 1] == "*":
                        converted_input_result[row][col] += 1
    total[count].extend(converted_input_result)
    count += 1

for i in total:
    for j in i:
        for k in j:
            print(k, end="")
        print("\n")
    print("\n\n")
