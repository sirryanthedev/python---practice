def binary_search(array: list, target):
    # NOTE: ASSUME ARRAY IS SORTED!
    # keep track of left and right limits (indeces)
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = left + ((right - left) // 2) # or less secure: (l + r) // 2
        if array[mid] == target:
            return True # target found
        # adjust right and left accordingly
        elif target < array[mid]:
            right = mid - 1
        else: # target > array[mid]
            left = mid + 1
    # no returns in loop -> return False for not found
    return False
