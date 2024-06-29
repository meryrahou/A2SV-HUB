# Problem: Operations on graphs - https://basecamp.eolymp.com/en/problems/2472

n = int(input())

ops = int(input())
from collections import defaultdict
my_dict = defaultdict(list)

for i in range(ops):
    op = list(map(int, input().split()))
    operation = op[0]
    if operation == 1:
        my_dict[op[1]].append(op[2])
        my_dict[op[2]].append(op[1])
    else:
        print(*my_dict[op[1]])