def list_binary(n):
    all_combinations = []
    s = []
    def dfs():
        if len(s) == n:
            all_combinations.append(s.copy())
            return
        for option in "01":
            s.append(option)
            dfs()
            s.pop()
    dfs()
    return all_combinations
