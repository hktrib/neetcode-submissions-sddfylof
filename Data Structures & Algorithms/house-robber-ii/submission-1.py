class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
            Whatever my answer I cannot 
            first and last answer
        '''

        if len(nums) == 1:
            return nums[0]

        def helper(arr: List[int]):
            prev = arr[0]
            prev2prev = 0

            for i in range(1, len(arr)):
                take = arr[i]
                if i > 1:
                    take += prev2prev 
                notTake = 0 + prev

                prev2prev = prev
                prev = max(take, notTake)
            return prev
        
        
        return max(nums[0], helper(nums[:len(nums) - 1]), helper(nums[1:]))

        