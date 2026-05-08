class Solution:
    def rob(self, nums: List[int]) -> int:
        # tabulation
        tab = [0 for _ in range(len(nums))]
        tab[0] = nums[0]

        for i in range(1, len(nums)):
            take = nums[i]
            if (i - 2) >= 0:
                take += tab[i - 2]
            not_take = 0 + tab[i - 1]

            tab[i] = max(take, not_take)
        
        return tab[len(nums) - 1]