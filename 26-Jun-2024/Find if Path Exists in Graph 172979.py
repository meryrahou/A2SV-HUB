# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited = set()

        def dfs(curr, visited):
            if curr == destination:
                return True

            visited.add(curr)

            for neighbor in graph[curr]:
                if neighbor  not in visited :
                    if dfs(neighbor, visited):
                        return True
            return False

        return dfs(source, visited)



        
