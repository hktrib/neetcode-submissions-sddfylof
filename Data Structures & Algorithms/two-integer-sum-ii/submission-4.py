class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # l = 0 
        # r = len(numbers) - 1

        # while l < r:
        #     if numbers[l] + numbers[r] > target:
        #         r -= 1
        #     elif numbers[l] + numbers[r] < target:
        #         l += 1
        #     else:
        #         return [l + 1, r + 1]


        # return []


        hm = dict()

        for i, num in enumerate(numbers):
            addend = target - num
            if addend in hm:
                return [hm[addend] + 1, i + 1]
            hm[num] = i
        
        return []


