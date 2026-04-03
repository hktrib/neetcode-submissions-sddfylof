class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [x for x in range(1, n + 1)]
        print(nums)

        res = []

        def dfs(i, c):
            if len(c) == k:
                res.append(c.copy())
                return
            if len(nums) - i < k - len(c):
                return

            c.append(nums[i])
            dfs(i + 1, c)
            c.pop()

            dfs(i + 1, c)
            
        dfs(0, [])

        return res