# Problem: Reshape the Matrix - https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        if m * n != r * c:
            return mat
        
        reshaped = [[0] * c for _ in range(r)]
        
        row = col = 0
        for i in range(m):
            for j in range(n):
                reshaped[row][col] = mat[i][j]
                col += 1
                if col == c:
                    col = 0
                    row += 1
        
        return reshaped