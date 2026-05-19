class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # maxIndex = 0
        # i = 0
        # while i <= maxIndex and i != len(nums) - 1:
        #     maxIndex = max(maxIndex,i + nums[i])
        #     i += 1
        #     print(maxIndex, i)

        # return maxIndex >= (len(nums) - 1)

        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return goal == 0