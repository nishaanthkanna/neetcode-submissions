class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = prices[0] # best buy price
        max_profit = 0
        for s in prices:
            # profit if sold today
            profit = s - b
            max_profit = max(max_profit, profit)
            # pick the lowest buy price
            b = min(b, s)
        return max_profit
            



        






        