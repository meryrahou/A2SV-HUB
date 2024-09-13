# Problem: Knight Probability in Chessboard - https://leetcode.com/problems/knight-probability-in-chessboard/

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [(-2, -1), (-2, +1), (+2, -1), (+2, +1), 
                  (-1, -2), (-1, +2), (+1, -2), (+1, +2)]
    
        dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(k + 1)]
        
        dp[0][row][column] = 1
        
        for step in range(1, k + 1):
            for r in range(n):
                for c in range(n):
                    for dr, dc in directions:
                        new_r, new_c = r + dr, c + dc
                        if 0 <= new_r < n and 0 <= new_c < n:
                            dp[step][r][c] += dp[step - 1][new_r][new_c] / 8
        
        total_probability = 0
        for r in range(n):
            for c in range(n):
                total_probability += dp[k][r][c]
        
        return total_probability