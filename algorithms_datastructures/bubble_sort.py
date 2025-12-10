# bubble sort - sort an array of numbers from low to high

def bubble_sort(array: list) -> list:
    """ bubble sort

    Args:
        array (list): list of numbers

    Returns:
        list: return list of numbers, sorted from low to high
    """
    size = len(array)
    swapped = 1
    while swapped:
        swapped = 0
        for i in range(size - 1):
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
                swapped = 1
        size -= 1
    return array
