class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Recursion
        maxL = len(cost)
        maxVal = float('inf')

        helperArr = [-1 for _ in range(maxL)]

        def helper(i):
            if i >= maxL:
                return 0
            if helperArr[i] != -1:
                return helperArr[i]

            left = helper(i + 1) + cost[i]
            right = helper(i + 2) + cost[i]

            helperArr[i] = min(left, right)

            return min(left, right)

        return int(min(helper(0), helper(1)))