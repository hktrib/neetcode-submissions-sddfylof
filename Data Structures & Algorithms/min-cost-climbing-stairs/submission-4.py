class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Tabulation
        maxL = len(cost)
        maxVal = float('inf')

        helperArr = [-1 for _ in range(maxL)]

        helperArr[0] = cost[0]
        helperArr[1] = cost[1]

        # 1, 2, 3
        # 1, 2, 3

        for i in range(2, maxL):
            leftSide = helperArr[i - 1] + cost[i]
            rightSide = cost[i] + helperArr[i - 2]

            helperArr[i] = min(leftSide, rightSide)

        return min(helperArr[maxL - 1], helperArr[maxL - 2])