class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
    #    hmap = dict()

    #    for num in nums:
    #         if num in hmap:
    #             return True
    #         else:
    #             hmap[num] = 0
    #     return False

        if len(nums) <= 1:
            return False

        nums = sorted(nums)

        for i in range(len(nums)):
            if nums[i] == nums[(i + 1 ) % len(nums)]:
                return True
        return False