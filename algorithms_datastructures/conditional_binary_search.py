# conditional binary search

def binary_search(arr: list):
    L = 0   # left
    R = len(arr) - 1  # right

    while L < R:
        M = L + ((R - L) // 2)
        if arr[M]:
            R = M
        else:
            L = M + 1
    return L

# print(binary_search([False, False, True, True]))
# output: 2 (first occurrence of True)
