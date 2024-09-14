# Problem: Odd Sum - https://codeforces.com/problemset/problem/797/B

n = int(input())
nums = list(map(int, input().split()))

odd_nums = []
best_odd_sum = 0

for n in nums:
    if n % 2 == 0 and n > 0:
        best_odd_sum += n
    elif n % 2 != 0:
        odd_nums.append(n)


odd_nums.sort(reverse=True)
best_odd_sum += odd_nums[0]
cpt = 1

for i in range(1, len(odd_nums)):
    if odd_nums[i] < 0:
        break
    best_odd_sum += odd_nums[i]
    cpt += 1


if best_odd_sum % 2 == 0:
    if cpt == len(odd_nums):
        best_odd_sum -= odd_nums[cpt-1]
    else:
        best_odd_sum += max(- odd_nums[cpt-1], odd_nums[cpt])

print(best_odd_sum)
