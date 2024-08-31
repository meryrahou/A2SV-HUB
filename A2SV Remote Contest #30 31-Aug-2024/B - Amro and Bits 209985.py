# Problem: B - Amro and Bits - https://codeforces.com/gym/545837/problem/B

t = int(input())
for _ in range(t):
    x = int(input())
    mask = x & -x
    if x & (x - 1) == 0:
        mask |= x + 1
    
    print(mask)
