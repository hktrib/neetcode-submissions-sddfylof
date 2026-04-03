class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []

        nums = sorted(nums)

        # [-1, -2, 3, 4, 5] 

        # List[List[int]] to be returned!
        threeSumList = []

        for index, val in enumerate(nums):

            # if val is greater than 0 then a 3Sum for 0 is impossible as all numbers
            # after it are also greater than 0 due to sorted(nums)
            if val > 0:
                break

            # if the previous 'target' value for the new 3Sum is the same we skip to avoid
            # duplicate triplets
            if index > 0 and val == nums[index - 1]:
                continue

            # The Target value is the negative of val so on summation we get 0
            target = 0 - val
            l = index + 1
            r = len(nums) - 1
            while l < r: 
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    # After we find a working triplet we push it and shift our two pointer 
                    # indices by one in their respective directions to see if a new two sum 
                    # can be generated for the same 'target'
                    threeSumList.append([val, nums[l], nums[r]])
                    l += 1 
                    r -= 1

                    # We keep incrementing l if we have seen it before
                    # we only have to make sure one of l or r doesnt point to a duplicate value
                    # so that way the same two sum doesnt get generated
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1


        return threeSumList