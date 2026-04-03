class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(c, n):
            if len(n) == 0:
                res.append(c.copy())
                return
            else:
                for i in range(len(n)):
                    c.append(n[i])
                    dfs(c, n[:i] + n[i + 1:])
                    c.pop()

        dfs([], nums)        
        
        return res