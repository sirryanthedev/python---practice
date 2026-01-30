def flattened(array: list) -> list[str]:
    """flatten list (of (sub)lists) to a list of strings

    Args:
        array (list): input list, possibly nested

    Returns:
        list[str]: flat list where each element is a string
    Doctest:
    >>> flattened([['str1', ['str2']], ['str3']])
    ['str1', 'str2', 'str3']
    """
    result = []
    def dfs(array):
        # base case: element is of type str
        if isinstance(array, str):
            result.append(array)
            return
        # loop through elements of array recursively
        for element in array:
            dfs(element)
    # initial call to start dfs
    dfs(array)
    # list[str] flattened list
    return result