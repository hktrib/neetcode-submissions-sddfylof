class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k > len(nums):
            return 0

        nums = [-x for x in nums]

        heapq.heapify(nums)
        kth = 0
        while k > 0:
            val = heapq.heappop(nums)
            print(nums)
            if k == 1:
                kth = val * -1
            
            k -= 1

        return kth
        