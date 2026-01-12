def filter_even(numbers: list):
    """yield all even numbers from a list

    Args:
        numbers (list): a list of numbers

    Yields:
        _type_: even number
    """
    yield from (number for number in numbers if number % 2 == 0) # generator expression - yield from can be replaced by "return"

for number in filter_even([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]):
    print(number)