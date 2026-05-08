class Solution:
    def rob(self, nums: List[int]) -> int:
        # memoization
        memo = [-1 for _ in range(len(nums))]

        def helper(i):
            if i < 0:
                return 0
            elif memo[i] != -1:
                return memo[i]
            else:
                take = nums[i] + helper(i - 2)
                not_take = 0 + helper(i - 1)

                memo[i] = max(take, not_take)
                return memo[i]
            
        
        return helper(len(nums) - 1)