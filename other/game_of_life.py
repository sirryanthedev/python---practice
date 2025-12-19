# (ex. Game of life - Dodona)

def toonGeneratie(generation: list) -> None:
    # create list with items to print
    to_print = []
    # add #rows in generation to to_print
    for row in generation:
        to_print.append([])

    # loop through generation list per row from left to right
    for row in range(len(generation)):
        for col in range(len(generation[0])):
            # X if alive (True)
            if generation[row][col] == True:
                to_print[row].append("X")
            # O if dead (False)
            elif generation[row][col] == False:
                to_print[row].append("O")
            else:
                print("Error: list values must be True or False!")
                break
    # print all elements of to_print, row per row, each row ending with ""
    for row in range(len(to_print)):
        for col in range(len(to_print[0])):
            print(to_print[row][col], end="")
            if col != len(to_print[0]) - 1:
                print(" ", end="")
        print() # print() instead of print("\n") because print() automatically adds a newline and to avoid 2 newlines

def aantalBuren(generation: list, i: int, j: int) -> int:
    # initialise neighbours (who are alive)
    adjacent_alive = 0

    # checks: if alive increment adjacent_alive by 1 per neighbour

    # chech top neighbour if possible
    if i > 0:
        if generation[i - 1][j] == True:
            adjacent_alive += 1

    # check bottom neighour if possible
    if i < len(generation) - 1:
        if generation[i + 1][j] == True:
            adjacent_alive += 1

    # check right neighbour if possible
    if j < len(generation[0]) - 1:
        if generation[i][j + 1] == True:
            adjacent_alive += 1

    # check left neighbour if possible
    if j > 0:
        if generation[i][j - 1] == True:
            adjacent_alive += 1

    # check top-right neighbour if possible
    if i > 0 and j < len(generation[0]) - 1:
        if generation[i - 1][j + 1] == True:
            adjacent_alive += 1
    
    # check top-left neighbour if possible
    if i > 0 and j > 0:
        if generation[i - 1][j - 1] == True:
            adjacent_alive += 1

    # check bottom-right neighbour if possible
    if i < len(generation) - 1 and j < len(generation[0]) - 1:
        if generation[i + 1][j + 1] == True:
            adjacent_alive += 1
    
    # check bottom-left neighbour if possible
    if i < len(generation) - 1 and j > 0:
        if generation[i + 1][j - 1] == True:
            adjacent_alive += 1

    return adjacent_alive

def volgendeGeneratie(generation: list) -> list:
    # create a new list for the next generation with as many rows as in the argument list
    next_gen = []
    for row in generation:
        next_gen.append([])

    # loop through columns per row of argument list, apply rules, and based on that form the next gen
    for row in range(len(generation)):
        for col in range(len(generation[0])):
            if generation[row][col] == True:
                if  1 < aantalBuren(generation, row, col) < 4: # if aantalBuren(generation) == 2 or aantalBuren(generation) == 3
                    next_gen[row].append(True)  # alive in next gen
                elif aantalBuren(generation, row, col) < 2 or aantalBuren(generation, row, col) > 3:
                    next_gen[row].append(False) # dead in next gen
            elif generation[row][col] == False:
                if aantalBuren(generation, row, col) == 3:
                    next_gen[row].append(True)  # alive in next gen
                else:
                    next_gen[row].append(False) # dead in next gen
            else:
                raise ValueError("Something went wrong...")

    return next_gen

generatie = [[True] + [False] * 7 for _ in range(6)]
toonGeneratie(generatie)