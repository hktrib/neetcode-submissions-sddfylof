class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(nums[l], res)
                # break
            m = ((r + l) // 2)
            print(f"M: {m}")
            res = min(nums[m], res)

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        
        return res