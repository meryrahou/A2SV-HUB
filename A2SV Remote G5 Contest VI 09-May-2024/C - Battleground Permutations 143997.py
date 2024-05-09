# Problem: C - Battleground Permutations - https://codeforces.com/gym/510902/problem/C

testcases = int(input())

mod = 1_000_000_007

for _ in range(testcases):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    total = 1

    pb = 0
    for pa in range(n):
        while pb < n and a[pa] > b[pb]:
            pb += 1

        total *= pb - pa
        total %= mod

    print(total)