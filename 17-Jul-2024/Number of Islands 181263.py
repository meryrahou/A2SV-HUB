# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [ [0 for i in range(m)] for i in range(n)]

        def inbound(row, col):
            return 0 <= row < n and 0 <= col < m

        def dfs(row, col, visited):
            visited[row][col] = 1

            for r,c in [(0,1), (1,0), (-1,0), (0,-1)]:
                if inbound(row+r, col+c) and not visited[row+r][col+c] and grid[row+r][col+c] == "1":
                    dfs(row+r, col+c, visited)
            

        islands = 0
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == "1":
                    dfs(i,j,visited)
                    islands += 1
        
        return islands
