class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxK = 0
        for i, pile in enumerate(piles):
            maxK = max(pile, maxK)


        l = 1
        r = maxK
        res = r
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                res = min(r, k)
                r = k - 1
            else:
                l = k + 1
            
        return res

