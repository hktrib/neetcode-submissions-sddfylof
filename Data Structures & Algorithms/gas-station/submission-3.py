class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            # Not Possible to complete circuit
            return -1
        else:
            # Possible to complete circuit
            index = len(gas) - 1
            profit = 0
            for i in range(len(gas)):
                profit += (gas[i] - cost[i])
                if profit < 0:
                    index = i + 1
                    profit = 0
                else:
                    index = min(i, index)
            return index