# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        def get_position(square):
            row = (square - 1) // n
            col = (square - 1) % n
            if row % 2 == 0:  # Left to right
                return n - 1 - row, col
            else:  # Right to left
                return n - 1 - row, n - 1 - col
        
        # BFS init
        queue = deque([(1, 0)])  # (current square, number of moves)
        visited = set()
        visited.add(1)
        
        while queue:
            curr_square, moves = queue.popleft()
            
            # If we reach the last square, return the number of moves
            if curr_square == n * n:
                return moves
            
            # Try all possible dice rolls (1 to 6)
            for next_square in range(curr_square + 1, min(curr_square + 6, n * n) + 1):
                r, c = get_position(next_square)
                
                # If there's a snake or ladder, move to its destination
                if board[r][c] != -1:
                    next_square = board[r][c]
                
                # If not visited, add to the queue
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))
        
        return -1
