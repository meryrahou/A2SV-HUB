# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degree = [0] * n
        
        for edge in edges:
            from_node, to_node = edge
            in_degree[to_node] += 1
        
        result = []
        for node in range(n):
            if in_degree[node] == 0:
                result.append(node)
        
        return result
