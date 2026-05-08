class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = [-1 for _ in range(len(nums))]

        def helper(i):
            if i >= len(nums):
                return 0
            elif memo[i] != -1:
                return memo[i]
            else:
                take = nums[i] + helper(i + 2)
                notTake = 0 + helper(i + 1)

                memo[i] = max(take, notTake)
                return memo[i]
            
        
        return helper(0)