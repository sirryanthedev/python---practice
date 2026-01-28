def subsets_p(nums: list):
    subset = []
    def dfs(i):
        # base case: index out of bounds
        if i >= len(nums):
            print(subset)
            return

        subset.append(nums[i])
        dfs(i + 1)
        subset.pop()
        dfs(i + 1)
    dfs(0)