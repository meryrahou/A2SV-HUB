# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        directions = {
            1: [(0, -1), (0, 1)],   # left, right
            2: [(-1, 0), (1, 0)],   # up, down
            3: [(0, -1), (1, 0)],   # left, down
            4: [(0, 1), (1, 0)],    # right, down
            5: [(0, -1), (-1, 0)],  # left, up
            6: [(0, 1), (-1, 0)]    # right, up
        }

        def dfs(x, y):
            if (x, y) == (m - 1, n - 1):  
                return True
            
            visited.add((x, y))
            for dx, dy in directions[grid[x][y]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    if (-dx, -dy) in directions[grid[nx][ny]]:
                        if dfs(nx, ny):
                            return True
            return False

        visited = set()
        return dfs(0, 0)