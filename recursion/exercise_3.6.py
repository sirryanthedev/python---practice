# (ex. 3.6.)

def nmsubsets(n: int, m: int) -> None:
    # (!) assignment conditions: n > 0, m >= 0

    # list of numbers from n to 0 (0 excluded)
    data = [num for num in range(n, 0, -1)]

    # list to keep track of current sublist
    current = []

    def dfs(i):
        # base case: i >= len(data) -> return to prevent index related problems
        if i >= len(data):
            # only print when length of current sublist equals m or when sublist is empty
            if len(current) == m or len(current) == 0:
                for num in current:
                    print(num, end=" ") # print each item seperated by a space on a unique line
                print() # after subset content print, print newline to seperate sublist contents
            return
        
        # include data[i]
        current.append(data[i])
        dfs(i + 1)

        # exclude data[i]
        current.pop()
        dfs(i + 1)
    
    # call depth-first search function with index 0 to start the search correctly
    dfs(0)

# function call, e.g.
# nmsubsets(5, 3)

# expected output:
# 5 4 3 
# 5 4 2
# 5 4 1
# 5 3 2
# 5 3 1
# 5 2 1
# 4 3 2
# 4 3 1
# 4 2 1
# 3 2 1
# (and a newline here for the empty sublist)