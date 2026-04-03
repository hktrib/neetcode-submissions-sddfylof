class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest = prices[0]

    

        for price in prices:
            lowest = min(lowest, price)

            max_profit = max(price - lowest, max_profit)

        return max_profit

        