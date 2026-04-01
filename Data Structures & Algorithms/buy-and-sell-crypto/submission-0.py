class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            min_buy = min(min_buy, prices[i])
            profit = prices[i] - min_buy
            max_profit = max(max_profit, profit)
        print(max_profit)
        if max_profit > 0:
            return max_profit
        return 0 

