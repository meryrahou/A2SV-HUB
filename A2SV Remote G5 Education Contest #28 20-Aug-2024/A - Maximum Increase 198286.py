# Problem: A - Maximum Increase - https://codeforces.com/gym/543262/problem/A

n = int(input())

a = list(map(int, input().split()))

length = 0
max_length = 0

for i in range(1, n):
    if a[i] > a[i-1]:
        length += 1
    else:
        max_length = max(max_length, length)
        length = 0

max_length = max(max_length, length)
print(max_length+1)
        