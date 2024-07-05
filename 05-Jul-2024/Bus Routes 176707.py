# Problem: Bus Routes - https://leetcode.com/problems/bus-routes/

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        graph = defaultdict(list)
        for stop in range(len(routes)): 
            for bus in routes[stop]:
                graph[bus].append(stop)

        bfs = deque()
        bus_visited = set()
        stop_visited = set()

        bfs.appendleft([source, 0])
        bus_visited.add(source)

        while bfs:
            bus, depth = bfs.pop()

            if bus == target: 
                return depth
            
            for stop in graph[bus]:
                if stop not in stop_visited: 
                    stop_visited.add(stop)

                    for bus_new in routes[stop]:
                        if bus_new not in bus_visited: 
                            bus_visited.add(bus_new)

                            bfs. appendleft([bus_new, depth+1])
        
        return -1