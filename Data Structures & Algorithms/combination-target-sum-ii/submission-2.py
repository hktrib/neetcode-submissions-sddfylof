class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []


        def dfs(i, c, rsum):
            if rsum == target:
                res.append(c.copy())
                return
            elif i >= len(candidates) or rsum > target:
                return
            else:
                c.append(candidates[i])
                dfs(i + 1, c , rsum + candidates[i])
                c.pop()

                while (i + 1 < len(candidates) and 
                    candidates[i] == candidates[i + 1]):
                    i += 1


                dfs(i + 1, c, rsum)

        dfs(0, [], 0)
        return res