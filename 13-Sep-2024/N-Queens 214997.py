# Problem: N-Queens - https://leetcode.com/problems/n-queens/description/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row):
            if row == n:
                # If all queens are placed, add the board configuration to results
                board = []
                for i in range(n):
                    row = ['.'] * n
                    row[queens[i]] = 'Q'
                    board.append(''.join(row))
                result.append(board)
                return
            
            for col in range(n):
                if col in cols or (row - col) in diagonals1 or (row + col) in diagonals2:
                    continue  

                queens[row] = col
                cols.add(col)
                diagonals1.add(row - col)
                diagonals2.add(row + col)

                backtrack(row + 1)

                # Backtrack: remove the queen and undo the changes
                cols.remove(col)
                diagonals1.remove(row - col)
                diagonals2.remove(row + col)

        result = []
        queens = [-1] * n  # queens[i] will store the column index where the queen is placed in row i
        cols = set()  # Columns under attack
        diagonals1 = set()  # Major diagonals under attack (row - col)
        diagonals2 = set()  # Minor diagonals under attack (row + col)

        backtrack(0)
        return result
