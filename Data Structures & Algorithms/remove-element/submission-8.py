class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = []
        for num in nums:
            if num != val:
                res.append(num)

        nums[:] = res

        return len(nums)