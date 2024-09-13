# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r, c))  # Add rotten orange to the queue
                elif grid[r][c] == 1:
                    fresh_count += 1  # Count fresh oranges
        
        if fresh_count == 0:
            return 0
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        minutes_passed = 0
        
        #  BFS
        while queue:
            minutes_passed += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        # Rot this fresh orange
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr, nc))
        
        # If there are fresh oranges left, return -1
        return minutes_passed - 1 if fresh_count == 0 else -1