# Problem: A - Nene's Game - https://codeforces.com/gym/523225/problem/A

testcases = int(input())

for _ in range(testcases):
    k, q = map(int, input().split())

    a = list(map(int, input().split()))
    ns = list(map(int, input().split()))

    res = []

    for n in ns:
        acop = a.copy()
        while acop and n > 0:
            if acop[-1] > n:
                acop.pop()
            else:
                n -= len(acop)
        res.append(n)
    print(*res)

