def print_sublists_sum(nums: list, target: int):
    sublist = []
    def dfs(i):
        if i >= len(nums):
            if sum(sublist) == target:
                print(sublist)
            return
        
        sublist.append(nums[i])
        dfs(i + 1)
        sublist.pop()
        dfs(i + 1)
    dfs(0)