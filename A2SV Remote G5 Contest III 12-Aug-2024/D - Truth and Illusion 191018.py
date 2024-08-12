# Problem: D - Truth and Illusion - https://codeforces.com/gym/505936/problem/D

t = int(input())

for _ in range(t):
    n = int(input())
    
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().strip())))
    
    total_operations = 0

    # Loop through the necessary cells (upper left quadrant including center line)
    for i in range(n // 2):
        for j in range((n + 1) // 2):
            # Positions of the four symmetric cells
            cell1 = grid[i][j]
            cell2 = grid[j][n - 1 - i]
            cell3 = grid[n - 1 - i][n - 1 - j]
            cell4 = grid[n - 1 - j][i]
            
            ones_count = cell1 + cell2 + cell3 + cell4
            
            min_flips = min(ones_count, 4 - ones_count)
            
            total_operations += min_flips
    
    print(total_operations)
