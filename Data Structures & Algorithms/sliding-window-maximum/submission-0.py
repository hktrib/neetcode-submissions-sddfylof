class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        output = []

        for i in range(len(nums)):
            # we do -nums[i] since heapq is by default a min-heap
            # and we need to make it function as a maxHeap
            heapq.heappush(heap, (-nums[i], i))

            '''
                What does i >= k - 1 indicate?
                i is k or more elements from the start

                take nums = [1,4,3,5,7,6], k = 3

                i = 5, k = 3 -> window = []

                while heap[0][1] <= i - k:

                heap[0][1] <= i - k indicates
                that the max element in heap is outside
                the k element range
                5 - 3 = 2 
                0 1 2 3 4 5
            '''
            if i >= k - 1:
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                output.append(-heap[0][0])
        return output