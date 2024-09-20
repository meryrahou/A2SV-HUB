# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                # Update the current element by choosing the minimum adjacent element from the row below
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        
        # The top element contains the minimum path sum
        return triangle[0][0]