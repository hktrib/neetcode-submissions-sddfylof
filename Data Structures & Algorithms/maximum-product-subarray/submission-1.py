class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        

        # Sum of Array
        # 

        res = nums[0]
        currMin, currMax = 1, 1

        for i in range(len(nums)):
            tmp = currMax * nums[i]
            currMax = max(nums[i] * currMax, nums[i] * currMin, nums[i])
            currMin = min(tmp, nums[i] * currMin, nums[i])
            res = max(res, currMax)
        return res