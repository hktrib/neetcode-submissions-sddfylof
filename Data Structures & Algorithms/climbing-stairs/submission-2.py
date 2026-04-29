class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        def helper(index: int) -> int:
            if index == 0:
                return 1
            elif index == 1:
                return 1
            elif dp[index] != 0:
                return dp[index]
            else:
                dp[index] = helper(index - 1) + helper(index - 2)
                return dp[index]
        
        return helper(n)