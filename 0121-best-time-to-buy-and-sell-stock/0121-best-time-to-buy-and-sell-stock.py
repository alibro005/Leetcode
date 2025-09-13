class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_Profit = 0
        min_Price = float("inf")
        n = len(prices)

        for i in range(0, n):
            min_Price = min(min_Price, prices[i])
            profit = prices[i] - min_Price
            max_Profit = max(profit, max_Profit)

        return max_Profit
