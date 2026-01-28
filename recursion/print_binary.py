def print_b(n):
    s = []
    def dfs():
        # base case: max combination length reached
        if len(s) == n:
            print("".join(s))
            return
        
        for ch in "01": # 01 are the options
            s.append(ch) # include option
            dfs() # call dfs
            s.pop() # exclude option
    dfs() # initial call