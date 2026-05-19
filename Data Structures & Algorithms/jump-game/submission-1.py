class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        maxIndex = 0
        i = 0
        while i <= maxIndex and i != len(nums) - 1:
            maxIndex = max(maxIndex,i + nums[i])
            i += 1
            print(maxIndex, i)

        return maxIndex >= (len(nums) - 1)
