class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        def dfs(idx, c, rsum):
            if rsum == target:
                res.append(c.copy())
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                elif rsum + candidates[i] > target:
                    return
                else:
                    c.append(candidates[i])
                    dfs(i + 1, c, rsum + candidates[i])
                    c.pop() # Clear out current combination for exclude case in next iteration

        dfs(0, [], 0)
        return res