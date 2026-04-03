class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solve this two ways

        hm = dict()

        for i in range(len(nums)):
            missing_addend = target - nums[i]
            
            if missing_addend in hm:
                return [hm[missing_addend], i]
            
            hm[nums[i]] = i
            print(hm)


        return []

