def quick_sort(sequence: list) -> list:
    if len(sequence) <= 1:
        return sequence
    pivot = sequence[0]
    left = [x for x in sequence[1:] if x <= pivot]
    right = [x for x in sequence[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

# test:
# print(quick_sort([5,4,1,2,3]))