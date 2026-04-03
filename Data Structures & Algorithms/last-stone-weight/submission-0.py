class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 1:
            stones.sort()

            x = stones[-1]
            y = stones[-2]

            if x < y:
                stones.pop(-1)
                stones[-1] = y - x
            elif x > y:
                stones.pop(-1)
                stones[-1] = x - y
            else:
                stones.pop(-1)
                stones.pop(-1)
            
        return stones[0] if stones else 0


