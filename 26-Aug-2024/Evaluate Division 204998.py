# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        
        for (A, B), value in zip(equations, values):
            graph[A][B] = value
            graph[B][A] = 1 / value
        
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0

            # Direct edge case
            if end in graph[start]:
                return graph[start][end]
            
            visited.add(start)
            
            # neighbors
            for neighbor in graph[start]:
                if neighbor not in visited:
                    weight = dfs(neighbor, end, visited)
                    if weight != -1.0:
                        return graph[start][neighbor] * weight
            
            return -1.0
        
        # queries
        results = []
        for C, D in queries:
            if C == D and C in graph:
                results.append(1.0)
            else:
                results.append(dfs(C, D, set()))
        
        return results