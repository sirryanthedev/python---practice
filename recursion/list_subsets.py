def subsets_list(nums: list):
    all_subsets = []
    subset = []
    def dfs(i):
        # base case: index out of bounds
        if i >= len(nums):
            all_subsets.append(subset.copy())
            return
        
        subset.append(nums[i]) # include nums[i]
        dfs(i + 1)
        subset.pop() # exclude nums[i]
        dfs(i + 1)
    dfs(0)
    return all_subsets