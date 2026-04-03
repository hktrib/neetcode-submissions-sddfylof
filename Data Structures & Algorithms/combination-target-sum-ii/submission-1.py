class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = set()

        # curr = []

        def dfs(i, c, rsum):
            if rsum == target:
                res.add(tuple(c.copy()))
                return
            elif i >= len(candidates) or rsum > target:
                return
            else:
                c.append(candidates[i])
                dfs(i + 1, c , rsum + candidates[i])

                c.pop()
                dfs(i + 1, c, rsum)

        dfs(0, [], 0)

        return [list(comb) for comb in res]