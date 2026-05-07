from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Recursion
        maxL = len(cost)
        maxVal = float('inf')

        @cache
        def helper(i):
            if i >= maxL:
                return 0

            left = helper(i + 1) + cost[i]
            right = helper(i + 2) + cost[i]

            return min(left, right)

        return int(min(helper(0), helper(1)))