# Problem: A - Algorithm Test I - https://codeforces.com/gym/544347/problem/A

from math import factorial

m = int(input())

ballons = list(map(int, input().split()))

n = len(ballons)

unique_colors = set(ballons)
print(factorial(len(unique_colors)))
