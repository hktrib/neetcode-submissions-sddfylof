class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solve this two ways

        # # Technique 1: HashMap
        # # Empty hashmap to store values together with indices
        # hm = dict()

        # # Looping through array 
        # for i, n in enumerate(nums):
        #     # compute the missing value to complete the sum
        #     missing_addend = target - n
            
        #     # check if missing value is already seen in prior iteration
        #     # and return [ missing_value's index, current index]
        #     # missing_value (since it was seen prior -> has smaller index)
        #     if missing_addend in hm:
        #         return [hm[missing_addend], i]
            
        #     # else we just record the current visited number as a potential
        #     # future missing addend
        #     hm[n] = i
        # return []


        # Technique 2: Two Pointer (requires sorting)
        

        sort_nums = sorted([(num, i) for i, num in enumerate(nums)])
        left = 0
        right = len(nums) - 1

        while left < right:
            s = sort_nums[left][0] + sort_nums[right][0]
            print(f"Sum = {s} | {sort_nums[left][0]} | {sort_nums[right][0]}")
            if s > target:
                right -= 1
            elif s < target:
                left += 1
            else:
                if sort_nums[left][1] < sort_nums[right][1]:
                    return [sort_nums[left][1], sort_nums[right][1]]
                else:
                    return [sort_nums[right][1], sort_nums[left][1]]
        
        return []




