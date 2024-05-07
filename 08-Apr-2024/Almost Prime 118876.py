# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

n = int(input())

# Function to count the number of distinct prime divisors of a number
def count_prime_divisors(num):
    count = 0
    for i in range(2, num + 1):
        if num % i == 0:
            while num % i == 0:
                num //= i
            count += 1
    return count

almost_prime_count = 0
for num in range(1, n + 1):
    if count_prime_divisors(num) == 2:
        almost_prime_count += 1

print(almost_prime_count)
