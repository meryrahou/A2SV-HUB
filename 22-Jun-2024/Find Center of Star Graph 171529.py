# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        first, second = edges[0], edges[1]
        
        if (first[0] == second[0]) or (first[0] == second[1]):
            return first[0]
        else :
            return first[1]