class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []


        def dfs(i, c, rsum):
            if rsum == target:
                res.append(c.copy())
                return
            elif i >= len(nums) or rsum > target:
                return
            else:
                c.append(nums[i])
                dfs(i, c, rsum + nums[i])
                c.pop()

                dfs(i + 1, c, rsum)

        dfs(0, [], 0)

        return res
