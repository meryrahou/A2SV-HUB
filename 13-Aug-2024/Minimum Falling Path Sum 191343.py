# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        dp = [ [0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[0][i] = matrix[0][i]

        # go through matrix and add minimum until end of it all
        for i in range(1,n):
            for j in range(n):
                top = dp[i-1][j] 
                top_left = dp[i-1][j-1] if j > 0 else float('inf')
                top_right = dp[i-1][j+1] if j < n-1 else float('inf')

                dp[i][j] = matrix[i][j] + min(top, top_left, top_right)

        return min(dp[n-1])
