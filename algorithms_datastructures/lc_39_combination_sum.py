# possible solution for leetcode 39 combination sum

def sublist_sum(candidates: list, target: int) -> list:
    """generate list of sublists which sum to target

    Args:
        candidates (list): elements to sum to target
        target (int): sum number

    Returns:
        list: sublist(s) which sum to target
    """
    # list which keeps track of results
    res = []
    # depth-first search fuction (i for pointer, current for current list, total for sum of current list)
    def dfs(i: int, current: list, total: int):
        # base case: if sum list == target, add sublist to result and return
        if total == target:
            res.append(current.copy())
            return
        # if pointer i out of bounds, or total of sublists > target: return
        if i >= len(candidates) or total > target:
            return

        # add option to current
        current.append(candidates[i])
        # call dfs for same i and current and modify total
        dfs(i, current, total + candidates[i])

        # pop last element and make sure candidates[i] is not included by calling dfs with i + 1
        current.pop()
        dfs(i + 1, current, total)

    # make sure dfs gets called internally with initialised values
    dfs(0, [], 0)
    return res