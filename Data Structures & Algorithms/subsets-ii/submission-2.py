class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        '''
            [1, 1, 2]

            First Branch:
            i = 0, c = []

            1. dfs on [1]
        '''

        def dfs(i, c):
            if i == len(nums):
                res.append(c[:])
                return
            
            c.append(nums[i])
            dfs(i + 1, c)
            c.pop()


            # Avoid starting a new branch with duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                print
                i += 1

            dfs(i + 1, c)


        dfs(0, [])

        return res