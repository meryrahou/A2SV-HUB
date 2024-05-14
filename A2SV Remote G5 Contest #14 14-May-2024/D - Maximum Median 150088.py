# Problem: D - Maximum Median - https://codeforces.com/gym/523225/problem/D

n, k = map(int, input().split())

a = list(map(int, input().split()))
a.sort()

med = n // 2

def checker(mid, med, n, k):
    less = 0
    for i in range(med, n):
        if a[i] >= mid:
            break
        less += mid - a[i]
    
    return (less <= k)

low, high = a[med], a[-1] + k

ans = low

while low <= high:
    mid = low + (high - low) // 2

    if checker(mid, med, n, k):
        ans = max(ans, mid)
        low = mid + 1
    else:
        high = mid - 1

print(ans)
