def combinations(n: int, current = "") -> None:
    """return all possible combinations of options e.g. 0 and 1 with length n

    Args:
        n (int): combination length
        current (str, optional): option buffer. Defaults to "".
    """
    if len(current) == n: # if combination length (n) equals length of buffer, print buffer
        print(current)
        return
    for option in "01": # options e.g. 0 and 1 for binary
        combinations(n, current + option)
