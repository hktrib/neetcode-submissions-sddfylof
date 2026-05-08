class Solution:
    def rob(self, nums: List[int]) -> int:
        # tabulation + space optimization

        prev = nums[0]
        prev2prev = 0

        for i in range(1, len(nums)):
            take = nums[i]
            if (i - 2) >= 0:
                take += prev2prev
            not_take = 0 + prev

            prev2prev = prev
            prev = max(take, not_take)
        
        return prev