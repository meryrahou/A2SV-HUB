# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

t = int(input())
for _ in range(t):
    x = int(input())
    mask = x & -x
    if x & (x - 1) == 0:
        mask |= x + 1
    
    print(mask)
