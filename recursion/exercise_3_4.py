def is_sum(S: set[int], m: int) -> bool:
    """
    Doctests:
    >>> is_sum({2,3,4}, 1)
    False
    >>> is_sum({2,3,4}, 2)
    True
    >>> is_sum({2,3,4}, 5)
    True
    >>> is_sum({0,2,3,8}, 7)
    True
    """
    if m == 0:
        return True
    if m < 0:
        return False

    for value in S:
        if value == 0:
            continue
        if is_sum(S, m - value):
            return True

    return False