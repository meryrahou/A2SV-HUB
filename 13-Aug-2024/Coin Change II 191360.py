# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)

        dp[0] = 1

        for coin in coins:
            # Update dp array for each amount from the coin's value to the target amount
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        
        return dp[amount]