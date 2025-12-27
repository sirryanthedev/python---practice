# (ex. 3.2.)

def sum_sublists_n(n: int) -> None:
    current = []
    def dfs(remaining, max_val):
        if remaining == 0:
            print(current)
            return
        for i in range(min(remaining, max_val), 0, -1):
            current.append(i)
            dfs(remaining - i, i)
            current.pop()
    dfs(n, n)
    return None

# function call e.g. 
print(sum_sublists_n(4))
# output:
# [4]
# [3, 1]
# [2, 2]
# [2, 1, 1]
# [1, 1, 1, 1]