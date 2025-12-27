# (ex. 3.7.)

def partitions(S: set[int]) -> list[list[set[int]]]:
    result = []
    elements = list(S)

    def dfs(i: int, current: list[set[int]]):
        # base case: all elements placed
        if i == len(elements):
            # deep copy of current partition
            result.append([block.copy() for block in current])
            return

        element = elements[i]

        # option 1: put element into existing blocks
        for block in current:
            block.add(element)
            dfs(i + 1, current)
            block.remove(element)

        # option 2: start new block
        current.append({element})
        dfs(i + 1, current)
        current.pop()

    dfs(0, [])
    return result