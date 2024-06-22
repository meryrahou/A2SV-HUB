# Problem: Cities and road - https://basecamp.eolymp.com/en/problems/992

nodes = int(input())
roads = 0
for i in range(nodes):
    roads += sum(list(map(int, input().split())))

print(int(roads/2))
    

