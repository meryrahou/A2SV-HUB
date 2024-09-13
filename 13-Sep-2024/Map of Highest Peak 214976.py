# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        
        height = [[-1] * n for _ in range(m)]
        queue = deque()
        
        # Add all water cells to the queue and set their height to 0
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                    queue.append((i, j))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            x, y = queue.popleft()
            
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                
                # If the new cell is within bounds and has not been visited
                if 0 <= new_x < m and 0 <= new_y < n and height[new_x][new_y] == -1:
                    # Assign height to this cell and add it to the queue
                    height[new_x][new_y] = height[x][y] + 1
                    queue.append((new_x, new_y))
        
        return height
