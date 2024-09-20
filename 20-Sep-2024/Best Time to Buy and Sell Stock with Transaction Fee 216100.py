# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        hold, cash = -prices[0], 0
        
        for i in range(1, n):
            hold = max(hold, cash - prices[i])
            cash = max(cash, hold + prices[i] - fee)
        
        return cash