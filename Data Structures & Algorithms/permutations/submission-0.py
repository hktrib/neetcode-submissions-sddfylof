class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(c, n):
            if n == []:
                res.append(c.copy())
                return

            for i in range(len(n)):
                c.append(n[i])

                if i + 1 < len(n):
                    dfs(c, n[:i] + n[i + 1:])
                else:
                    dfs(c, n[:i])
                c.pop()
        dfs([], nums)

        return res