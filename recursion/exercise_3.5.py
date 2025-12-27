# (ex. 3.5.)

def print_subsets(data: list) -> None:
    # list to keep track of sublist
    current = []

    # depth-first search function
    def dfs(i):
        if i >= len(data):
            # print each item in current sublist, seperated by a " "
            for item in current:
                print(item, end=" ")
            # print newline to seperate generated sublists from each other
            print()
            return

        # either include data[i]
        current.append(data[i])
        dfs(i + 1)

        # either exclude data[i]
        current.pop()
        dfs(i + 1)
    dfs(0)
    return None

# function call, e.g. with [1,2,3]
print_subsets([1,2,3])
# output:
# 1 2 3 
# 1 2
# 1 3
# 1
# 2 3
# 2
# 3
# (!) an empty line, which represents an empty subset, will be printed