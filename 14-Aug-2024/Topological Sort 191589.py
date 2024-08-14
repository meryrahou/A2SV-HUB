# Problem: Topological Sort - https://codeforces.com/problemset/gymProblem/101102/K

from collections import defaultdict

testcases = int(input())

for _ in range(testcases):
    n, m = map( int, input().split())
    graph = defaultdict(set)

    for _ in range(m):
        x, y = map(int, input().split())
        graph[y].add(x)

    res = [i for i in range(1,n+ 1)]
    for i in range(1, n+ 1):
        left = i - 2 
        while left >= 0 :
            if res[left] in graph[i]:
                res[left], res[left+ 1] = res[left+ 1], res[left]
                left -= 1
            else:
                break

    print(*res) 