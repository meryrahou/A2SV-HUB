# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n,m=len(matrix),len(matrix[0])

        left = 0 
        right = (n)*(m)-1
        while left<=right : 
            mid = (right+left)//2
            if n == 1  :
                i,j=0,mid
            elif m ==1 :
                i,j = mid,0
            else:
                i,j = divmod(mid,m)

            if matrix[i][j] == target : 
                return True
            elif matrix[i][j]> target :
                right = mid-1
            else :
                left = mid+1
        
        return False