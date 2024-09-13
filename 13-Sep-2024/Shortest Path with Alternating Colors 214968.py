# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in redEdges:
            graph[u].append((v, 'red'))
        for u, v in blueEdges:
            graph[u].append((v, 'blue'))
        
        distances = [[float('inf'), float('inf')] for _ in range(n)]  # distances[i] = [red_dist, blue_dist]
        distances[0] = [0, 0]  # Start from node 0 with both red and blue distances = 0
        
        queue = deque([(0, 'red'), (0, 'blue')])  # BFS starts with both red and blue edges
        
        while queue:
            node, last_color = queue.popleft()
            
            # Determine the next color to explore
            next_color = 'blue' if last_color == 'red' else 'red'
            
            for neighbor, edge_color in graph[node]:
                if edge_color == next_color:
                    if next_color == 'red' and distances[neighbor][0] == float('inf'):
                        distances[neighbor][0] = distances[node][1] + 1
                        queue.append((neighbor, 'red'))
                    elif next_color == 'blue' and distances[neighbor][1] == float('inf'):
                        distances[neighbor][1] = distances[node][0] + 1
                        queue.append((neighbor, 'blue'))
        
        result = []
        for red_dist, blue_dist in distances:
            min_dist = min(red_dist, blue_dist)
            result.append(min_dist if min_dist != float('inf') else -1)
        
        return result
