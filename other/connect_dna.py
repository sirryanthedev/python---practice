# (ex. connect dna - Dodona)

def find_horizontal(board):
    rows = len(board)
    cols = len(board[0])
    solutions = []

    for r in range(rows):
        for c in range(cols - 3):           # window of 4
            if board[r][c] == board[r][c+1] == board[r][c+2] == board[r][c+3]:
                solutions.append((r+1, c+1, "horizontally"))

    return solutions

def find_vertical(board):
    rows = len(board)
    cols = len(board[0])
    solutions = []

    for r in range(rows - 3):
        for c in range(cols):
            if board[r][c] == board[r+1][c] == board[r+2][c] == board[r+3][c]:
                solutions.append((r+1, c+1, "vertically"))

    return solutions

def findSolutions(board):
    horizontal = find_horizontal(board)
    vertical = find_vertical(board)
    all_solutions = horizontal + vertical

    return tuple(sorted(all_solutions))

def showSolutions(board):
    rows = len(board)
    cols = len(board[0])

    # print column numbers
    print("     ", end="")
    for c in range(1, cols+1):
        print(f"{c:>5}", end="")
    print()

    # print each row
    for r in range(rows):
        print(f"{r+1:>5}", end="")
        for c in range(cols):
            print(f"{board[r][c]:>5}", end="")
        print()

    # print solutions
    for r, c, direction in findSolutions(board):
        print(f"{r},{c} {direction}")

# For this task, we have devised an extension of the popular game Four-in-a-Row. Like the original game, our expansion is also played on a rectangular 
#  board game with 
#  rows and 
#  columns. In contrast to the original Four-in-a-Row game, our expansion can be played with more than two players. Each player must choose a letter of the alphabet to denote his pieces.

# In the example below, we illustrate the extension of the Four-in-a-Row game with a fully stocked 
#  game board on which four players have respectively chosen the letters A, C, G and T as their playing pieces. That's why we named this variant DNA-in-a-row.

# Assignment
# Write a function

# findSolutions(gameboard)
# that indicates the position of a Four-in-a-Row on a given board. The board must be passed to this function as a list of lists. Here, each element of the outer list is a row of the board. A row of the board is represented as a list of capitals.
# The function must return a tuple with all Four-in-a-Row positions. Each element of this tuple is a Four-in-a-Row position which is also presented as a tuple itself. Each set of four horizontal consecutive identical characters is represented as a tuple, the first two elements indicating the row and column number of the leftmost position of the series of four consecutive identical characters. The third element of the tuple is composed of the string horizontally . Analogously, each set of four vertically successive identical characters is represented as a tuple of three elements, of which the third element contains the string vertically, and the first two elements correspond with the row and column number of the upper position in the series of four successive equal letters. The elements of the tuple that is returned as the result of the function must be sorted in ascending order.

# Write a function

# showSolutions(gameboard)
# that prints both a formatted representation of the board as all positions with Four-in-a-Row to the output. To this function, a game board must be passed as argument, which is the same size as described in the findSolutions function.
# The printing of the board should be in the format illustrated in the example below. On the first row of the column numbers are printed above the columns of the board. The following rows each start with a row number followed by the letters that are printed to the corresponding positions of the board. Row and column numbers are indexed from 1. For each column of the output five character positions are reserved to be filled right-aligned.

# After showing the game board the positions with four consecutive identical characters are also printed. Obviously the function showSolutions will have to make use of the findSolutions function. The positions should be printed in the same order like in the tuple that is returned by the findSolutions function. The row and column number of each solution is written on a separate line, followed by a space and the direction of the solution (horizontally or vertically).

# Example
# >>> game board = [['T', 'T', 'T', 'A', 'C', 'C', 'G', 'A'],
# ...             ['C', 'C', 'G', 'T', 'C', 'G', 'T', 'A'],
# ...             ['T', 'C', 'A', 'T', 'T', 'G', 'T', 'G'],
# ...             ['T', 'G', 'C', 'G', 'C', 'G', 'C', 'G'],
# ...             ['C', 'G', 'T', 'G', 'C', 'C', 'G', 'T'],
# ...             ['A', 'T', 'T', 'T', 'T', 'G', 'G', 'C'],
# ...             ['A', 'T', 'C', 'T', 'T', 'A', 'T', 'A'],
# ...             ['A', 'T', 'G', 'G', 'C', 'T', 'T', 'C'],
# ...             ['T', 'T', 'C', 'A', 'C', 'C', 'G', 'T']]
# >>> findSolutions(game board)
# ((6, 2, 'horizontally'), (6, 2, 'vertically'))
# >>> showSolutions(game board)
#          1    2    3    4    5    6    7    8
#     1    T    T    T    A    C    C    G    A
#     2    C    C    G    T    C    G    T    A
#     3    T    C    A    T    T    G    T    G
#     4    T    G    C    G    C    G    C    G
#     5    C    G    T    G    C    C    G    T
#     6    A    T    T    T    T    G    G    C
#     7    A    T    C    T    T    A    T    A
#     8    A    T    G    G    C    T    T    C
#     9    T    T    C    A    C    C    G    T
# 6,2 horizontally
# 6,2 vertically
