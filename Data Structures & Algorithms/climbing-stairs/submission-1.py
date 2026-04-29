class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * n
        def helper(index: int) -> int:
            if index == n:
                return 1
            elif index > n:
                return 0
            elif dp[index] != 0:
                return dp[index]
            else:
                dp[index] = helper(index + 1) + helper(index + 2)
                return dp[index]
        
        return helper(0)