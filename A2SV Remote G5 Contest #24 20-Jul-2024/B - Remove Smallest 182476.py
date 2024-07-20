# Problem: B - Remove Smallest - https://codeforces.com/gym/536373/problem/B

testcase = int(input())

for _ in range(testcase):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    for i in range(1, n):
        if a[i] - a[i - 1] > 1:
            print("NO")
            break
    else:
        print("YES")