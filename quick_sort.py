# quick sort function

def quick_sort(sequence: list):
    # terminating condition: if sequence has length 1 or lower: return it (already sorted)
    if len(sequence) <= 1:
        return sequence
    
    # pivot is last item of sequence, remove (and return) it from sequence
    pivot = sequence.pop()

    greater_than_pivot = []
    less_than_pivot = []

    for item in sequence:
        if item < pivot:
            less_than_pivot.append(item)
        else:
            greater_than_pivot.append(item)
    
    # apply the function recursively to list of numbers less and greater than pivot
    return (quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot))