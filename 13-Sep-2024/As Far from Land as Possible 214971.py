# Problem: As Far from Land as Possible - https://leetcode.com/problems/as-far-from-land-as-possible/description/

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        queue = deque()
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
        
        # If there is no water or no land, return -1
        if len(queue) == 0 or len(queue) == n * n:
            return -1
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # BFS
        distance = -1
        while queue:
            distance += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    
                    # If it's within bounds and it's water (0)
                    if 0 <= new_x < n and 0 <= new_y < n and grid[new_x][new_y] == 0:
                        # Mark the water as visited by marking it as land (1)
                        grid[new_x][new_y] = 1
                        queue.append((new_x, new_y))
        
        return distance