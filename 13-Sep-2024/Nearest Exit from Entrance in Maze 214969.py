# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
    
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        queue = deque([(entrance[0], entrance[1], 0)])  # (row, col, steps)
        
        # Mark the entrance as visited by changing it to a wall
        maze[entrance[0]][entrance[1]] = '+'
        
        while queue:
            row, col, steps = queue.popleft()
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # new cell is within bounds and is an empty cell
                if 0 <= new_row < m and 0 <= new_col < n and maze[new_row][new_col] == '.':
                    # new cell is a border cell (but not the entrance), it's an exit
                    if new_row == 0 or new_row == m - 1 or new_col == 0 or new_col == n - 1:
                        return steps + 1
                    
                    # Mark new cell as visited and add it to the queue
                    maze[new_row][new_col] = '+'
                    queue.append((new_row, new_col, steps + 1))
        
        return -1