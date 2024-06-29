# Problem: Maximal Network Rank - https://leetcode.com/problems/maximal-network-rank/description/

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        road_count = [0] * n
        adjacency = defaultdict(set)

        for road in roads:
            u, v = road
            road_count[u] += 1
            road_count[v] += 1
            adjacency[u].add(v)
            adjacency[v].add(u)

        max_rank = 0

        for i in range(n):
            for j in range(i + 1, n):
                if j in adjacency[i]:
                    rank = road_count[i] + road_count[j] - 1
                else:
                    rank = road_count[i] + road_count[j]
                
                max_rank = max(max_rank, rank)
        
        return max_rank
