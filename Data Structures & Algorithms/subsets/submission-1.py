class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []


        def dfs(i, c):
            if i >= len(nums):
                res.append(c.copy())
                return
            else:
                c.append(nums[i])
                dfs(i + 1, c)
                c.pop()

                dfs(i + 1, c)
        
        dfs(0, [])

        return res