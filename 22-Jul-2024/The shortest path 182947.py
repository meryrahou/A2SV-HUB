# Problem: The shortest path - https://basecamp.eolymp.com/en/problems/4853

from collections import deque, defaultdict

def shortest_path(n, m, a, b, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    queue = deque([(a, 0)])
    distances = {a: 0}
    predecessors = {a: None}
    
    while queue:
        current, dist = queue.popleft()
        
        if current == b:
            path = []
            while current is not None:
                path.append(current)
                current = predecessors[current]
            path.reverse()
            print(dist)
            print(" ".join(map(str, path)))
            return
        
        for neighbor in graph[current]:
            if neighbor not in distances:
                distances[neighbor] = dist + 1
                predecessors[neighbor] = current
                queue.append((neighbor, dist + 1))
    
    print(-1)

n, m = map(int, input().split())
a, b = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

shortest_path(n, m, a, b, edges)
