# Problem: New Year Transportation - https://codeforces.com/problemset/problem/500/A

n, t = map(int, input().split())
 
a = list(map(int, input().split()))
 
curr = 0
while curr < n-1:
    # print(curr)
    if curr == t-1:
        print("YES")
        break
    curr += a[curr]
else:
    if curr == t-1:
        print("YES")
    else:
        print('NO')