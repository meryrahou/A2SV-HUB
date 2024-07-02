# Problem: Detonate the Maximum Bombs - https://leetcode.com/problems/detonate-the-maximum-bombs/description/

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)

        for b1, (x1,y1,r1) in enumerate(bombs):
            for b2, (x2,y2,r2) in enumerate(bombs):
                if b2 != b1 and r1 >= sqrt((x2-x1)** 2 + (y2-y1)** 2):
                    graph[b1].append(b2)
        
        print(graph)
        visited = set()
        def dfs(vertex, visited):
            q = 1

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q += dfs(neighbor, visited)

            return q
        
        mx = 0
        for node in range(len(bombs)):
            visited = set()
            visited.add(node)
            mx = max(mx, dfs(node,visited))

        return mx