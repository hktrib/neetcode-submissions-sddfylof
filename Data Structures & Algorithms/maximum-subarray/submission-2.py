class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Dynamic Programming

        global_max = float('-inf')

        def f(i, ):
            nonlocal global_max
            if i == 0:
                global_max = max(global_max, nums[0])
                return nums[0]
            else:
                l = nums[i] + f(i - 1)
                r = nums[i]

                curr_max = max(l, r)

                global_max = max(curr_max, global_max)
                return curr_max


        f(len(nums) -1)
        return global_max