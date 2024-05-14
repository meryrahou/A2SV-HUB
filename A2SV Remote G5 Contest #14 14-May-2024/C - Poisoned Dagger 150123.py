# Problem: C - Poisoned Dagger - https://codeforces.com/gym/523225/problem/C

testcase = int(input())

'''
instead of checking the diffs
looping the array
    we add to hit the min between the diff and mid

'''

def checker(mid,n,h):
    hit = 0
    for i in range(n):
        hit += min(a[i+1]-a[i], mid)

    return (hit >= h)


for _ in range(testcase):
    n, h = map(int, input().split())

    a = list(map(int, input().split()))
    a.append(float('inf'))

    low, high = 0, 10**18

    ans = high
    while low <= high:
        mid = (low + high) // 2

        if checker(mid, n, h):
            ans = min(ans, mid)
            high = mid - 1
        else:
            low = mid + 1

    print(ans)