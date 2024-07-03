# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1]* len(graph)

        def dfs(vertex):
            for neighbor in graph[vertex]:
                print(color , neighbor, vertex)
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[vertex]
                    if dfs(neighbor) == False:
                        return False
                else:
                    if color[vertex] == color[neighbor]:
                        return False
            return True

        for node in range(len(graph)):
            if color[node] == -1:
                color[node] = 0
                if dfs(node) == False:
                    print(color)
                    return False
        return True
