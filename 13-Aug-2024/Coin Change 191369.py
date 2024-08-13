# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for a in range(1, amount + 1):
            for coin in coins:

                if a - coin >= 0 :
                    dp[a] = min(dp[a], dp[a - coin] + 1)
        
        # If dp[amount] is still the large initial value, return -1
        if dp[amount] != amount + 1 :
            return dp[amount] 
        else:
            return -1