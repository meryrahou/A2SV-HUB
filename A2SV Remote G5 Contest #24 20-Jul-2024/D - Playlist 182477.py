# Problem: D - Playlist - https://codeforces.com/gym/536373/problem/D

n, k = map(int, input().split())
songs = []

for _ in range(n):
    t, b = map(int, input().split())
    songs.append((b, t))


songs.sort(reverse=True)

max_pleasure = 0
current_length = 0
lengths = []

import heapq

for b, t in songs:
    if len(lengths) < k:
        heapq.heappush(lengths, t)
        current_length += t
    else:
        if lengths[0] < t:
            current_length += t - heapq.heappop(lengths)
            heapq.heappush(lengths, t)
    
    max_pleasure = max(max_pleasure, current_length * b)

print(max_pleasure)
