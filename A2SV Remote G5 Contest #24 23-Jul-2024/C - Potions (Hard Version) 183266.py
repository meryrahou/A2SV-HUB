# Problem: C - Potions (Hard Version) - https://codeforces.com/gym/536373/problem/C

import heapq

n = int(input())
potions = list(map(int, input().split()))


h = 0
heap = []
count = 0

for potion in potions:
    if potion +h >= 0:
        h += potion 
        count += 1
        if potion < 0:
            heapq.heappush(heap, potion)
    elif heap and potion > heap [0] :
        bad_potion = heapq.heappop(heap) 
        h += - bad_potion
        h += potion 
        heapq.heappush (heap, potion)

print (count)