# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, og: List[List[int]]) -> int:
        m = len(og)        
        n = len(og[0])

        if og[0][0] == 1:
            return 0
        
        dp = [ [0] * n for _ in range(m)]
        dp[0][0] = 1

        #first row
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] if og[0][i] == 0 else 0
        #first col
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] if og[i][0] == 0 else 0

        #rest
        for i in range(1, m):
            for j in range(1, n):
                if og[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0
        
        return dp[m-1][n-1]


