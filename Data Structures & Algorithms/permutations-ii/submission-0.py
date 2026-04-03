class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        
        res = []

        def dfs(c, n):
            if len(c) == len(nums):
                res.append(c[:])
                return
            
            i = 0
            while i < len(n):
                c.append(n[i])
                dfs(c, n[:i] + n[i + 1 :])
                c.pop()
                while i + 1 < len(n) and n[i] == n[i + 1]:
                    i += 1

                i += 1

        dfs([], nums)
        return res
