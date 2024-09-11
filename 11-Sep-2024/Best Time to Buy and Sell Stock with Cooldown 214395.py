# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        
        hold = [0] * n  
        not_hold = [0] * n  
        cooldown = [0] * n  
        
        hold[0] = -prices[0]  
        not_hold[0] = 0  
        cooldown[0] = 0  
        
        for i in range(1, n):
            # Either keep holding or buy today
            hold[i] = max(hold[i-1], not_hold[i-1] - prices[i])  
            # Sell today and enter cooldown
            cooldown[i] = hold[i-1] + prices[i]  
            # Either stay in not_hold or come out of cooldown
            not_hold[i] = max(not_hold[i-1], cooldown[i-1])  
        
        return max(not_hold[n-1], cooldown[n-1])
