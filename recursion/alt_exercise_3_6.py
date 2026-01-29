# helper function
def unique_occurence(array: list, number: int) -> bool:
    count = 0;
    for item in array:
        if item == number:
            count += 1
    return (count == 1)

# helper function
def output_array(array: list) -> None:
    for item in array:
        print(item, end=" ")
    print()

# helper function
def array_is_descending(array: list) -> bool:
    current = False
    first = True
    for item in array:
        if first:
            current = item
            first = False
        elif current < item:
            return False
        current = item
    return True

# main function
def print_combinations(n: int, m: int) -> None:
    """generate unique, descending subsets of range(1, n) with length m

    Args:
        n (int): range
        m (int): length

    example: print_combinations(5, 3)
    expected output:
        3 2 1 
        4 2 1
        4 3 1
        4 3 2
        5 2 1
        5 3 1
        5 3 2
        5 4 1
        5 4 2
        5 4 3
    """
    subset = []
    def dfs():
        # base case, max length reached
        if len(subset) >= m:
            for x in subset:
                # loop through every item in the sublist and check for multiple occurences
                if not unique_occurence(subset, x):
                    return
                if not array_is_descending(subset):
                    return
            # if unique occurence (no return from block above) -> output array
            output_array(subset)
            return
        for num in range(1,n + 1):
            subset.append(num)
            dfs()
            subset.pop()
    dfs()