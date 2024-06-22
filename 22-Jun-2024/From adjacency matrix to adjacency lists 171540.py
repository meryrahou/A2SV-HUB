# Problem: From adjacency matrix to adjacency lists - https://basecamp.eolymp.com/en/problems/3981

nodes = int(input())
l = [[] for _ in range(nodes)]

for i in range(nodes):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        if row[j] == 1:
            l[i].append(j+1)
    print(len(l[i]), *l[i])


