# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        first_sum = ( target + total ) // 2

        if (target + total) % 2 != 0 or first_sum < 0:
            return 0

        dp = [0] * ( first_sum + 1 )
        dp[0] = 1

        for num in nums:
            for j in range(first_sum, num - 1, -1):
                dp[j] += dp[j - num]
        
        return dp[first_sum]
