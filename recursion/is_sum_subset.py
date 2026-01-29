def is_sum(S: set[int], n: int) -> bool:
    if n == 0:
        return True # sum found
    elif n < 0:
        return False # sum not found

    # loop through the elements of S and call the function recursively with n - element and S
    for element in S:
        if element > 0: # avoid infinite recursion
            if is_sum(S, n - element): # True returned in call
                return True # valid sum found recursively

    return False # if True not returned in block above, return False (no sum)

print(is_sum({1,2,3,0}, 5))