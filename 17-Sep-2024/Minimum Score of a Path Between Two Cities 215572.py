# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # adjacency list
        graph = defaultdict(list)
        for a, b, distance in roads:
            graph[a].append((b, distance))
            graph[b].append((a, distance))
        
        visited = [False] * (n + 1)
        queue = deque([1])
        visited[1] = True
        min_score = float('inf')
        
        # BFS
        while queue:
            city = queue.popleft()
            for neighbor, dist in graph[city]:
                # Track the minimum distance
                min_score = min(min_score, dist)  
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        
        return min_score