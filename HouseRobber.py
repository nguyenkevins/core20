class Solution:
    def rob(self, nums: List[int]) -> int:
        store = [-1] * len(nums)

        def dfs(i):
            if i < 0:
                return 0
            if store[i] != -1:
                return store[i]
            store[i] = max(nums[i] + dfs(i-2), dfs(i-1))
            return store[i]

        dfs(len(nums)-1)
        return store[len(nums)-1]
