# Problem: B - Divisibility by 2^n - https://codeforces.com/gym/522997/problem/B

testcases = int(input())

def pow_2(number):
    if number == 0:
        return 1
    
    if number % 2 != 0:
        return 0

    return 1 + pow_2(number // 2)

for _ in range(testcases):
    len = int(input())
    arr = list(map(int, input().split()))
    
    total = 0
    index_pow = []

    for i in range(len):
        total += pow_2(arr[i])
        index_pow.append(pow_2( i + 1 ))

    index_pow.sort(reverse=True)
    i = 0

    while total < len and i < len:
        total += index_pow[i]
        i += 1  

    if total < len:
        print(-1)
    else:
        print(i)