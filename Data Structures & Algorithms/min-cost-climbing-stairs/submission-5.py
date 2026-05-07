class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Tabulation
        maxL = len(cost)
        maxVal = float('inf')

        helperArr = [-1 for _ in range(maxL)]

        backTwo = cost[0]
        backOne = cost[1]

        # 1, 2, 3
        # 1, 2, 3

        for i in range(2, maxL):
            current = cost[i] + min(backOne, backTwo)

            backTwo = backOne
            backOne = current

        return min(backOne, backTwo)