class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        comb = [[], 0]

        def dfs(i):
            if i >= len(nums) or comb[1] > target:
                return
            elif comb[1] == target:
                res.append(comb[0].copy())
                return
            else:
                comb[1] += nums[i]
                comb[0].append(nums[i])

                dfs(i)
                # dfs(i + 1)

                comb[1] -= nums[i]
                comb[0].pop()

                dfs(i + 1)
        
        dfs(0)

        return res


