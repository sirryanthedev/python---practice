def subsets(data: list) -> list:
    """generate all possible sublists of a list

    Args:
        data (list): initial list

    Returns:
        list: list of all possible sublists of data
    """
    results = []    # list of all possible sublists
    subset = []

    # depth first search function - 2 options per position (incl. or excl.)
    def dfs(i):
        if i >= len(data):
            results.append(subset.copy())
            return

        # include data at index i
        subset.append(data[i])
        dfs(i + 1)

        # exclude data at index i
        subset.pop()
        dfs(i + 1)

    dfs(0)
    return results
