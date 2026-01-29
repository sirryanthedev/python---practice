def subsets_n(n: int) -> list[list]:
    result = []
    def dfs(remaining: int, current: list, max_val: int):
        # base case: target reached
        if remaining == 0:
            result.append(current.copy()) # add copy of partition to result
            return
        
        for i in range(1, min(remaining, max_val) + 1):
            dfs(remaining - i, current + [i], i) # remaining = remaining - i, concat current + i, max_val = i to avoid duplicates
    dfs(n, [], n) # initially call with remaining = n, current = empty list, max_val = n
    return result # all partitions which sum to n

print(subsets_n(4))
        