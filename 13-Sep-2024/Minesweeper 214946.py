# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        def countMines(r, c):
            count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'M':
                    count += 1
            return count
        
        def dfs(r, c):
            # If the current cell is not 'E', there's nothing to do
            if board[r][c] != 'E':
                return
            
            # Count adjacent mines
            mine_count = countMines(r, c)
            
            if mine_count == 0:
                # No adjacent mines, mark as 'B' and explore neighbors
                board[r][c] = 'B'
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        dfs(nr, nc)
            else:
                # There are adjacent mines, mark with the count
                board[r][c] = str(mine_count)
        
        click_row, click_col = click
        
        # If the clicked position is a mine, game over
        if board[click_row][click_col] == 'M':
            board[click_row][click_col] = 'X'
        else:
            dfs(click_row, click_col)
        
        return board
