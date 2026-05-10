class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
            Basically House Robber:
            
            Since first and last cannot be in their together
            we can slice the array into [:len(arr) - 1] & [1:]

            and we can do a return arr[0] of len(nums) if nums != 1

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
        
        
        return max(helper(nums[:len(nums) - 1]), helper(nums[1:]))

        