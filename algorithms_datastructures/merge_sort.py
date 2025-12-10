# merge sort algorithm

def merge_sort(array: list) -> list:
    
    # base case: if array has length less or equal to 1, no need to sort, just return it
    if len(array) <= 1:
        return array

    # middle point of the array
    mid = len(array) // 2

    # call merge sort on both left and right halves to split them further until terminating condition is met
    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])

    # now all final arrays have len 1
    merged = []
    i = j = 0

    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            merged.append(left_array[i])
            i += 1
        else:
            merged.append(right_array[j])
            j += 1
    
    # if anything left over in left or right array after creating sorted arrays: add it to merged array
    merged.extend(left_array[i:])
    merged.extend(right_array[j:])

    return merged
