# Problem: C - Rania And Her Inheritance - https://codeforces.com/gym/545837/problem/C

from collections import defaultdict

n, m = map(int, input().split())

experts = []
rivalries = []
for _ in range(n):
    experts.append(input())

for _ in range(m):
    rivalry = list(input().split(" "))
    rivalries.append(rivalry)

# adjacency matrix n x n
index = {experts[i]: i for i in range(n)}  
rivalries_matrix = [[False] * n for _ in range(n)]  
for a, b in rivalries:
    i, j = index[a], index[b]
    rivalries_matrix[i][j] = True
    rivalries_matrix[j][i] = True


# bitmasking 
max_team_size = 0
best_team_mask = 0

for mask in range(1 << n):  
    valid_team = True
    for i in range(n):
        if not (mask & (1 << i)):
            continue  
        for j in range(i + 1, n):
            if (mask & (1 << j)) and rivalries_matrix[i][j]:
                valid_team = False
                break
        if not valid_team:
            break

    if valid_team:
        team_size = bin(mask).count('1')  
        if team_size > max_team_size:
            max_team_size = team_size
            best_team_mask = mask



best_team = [experts[i] for i in range(n) if best_team_mask & (1 << i)]
best_team.sort()

print(max_team_size)
for expert in best_team:
    print(expert)
