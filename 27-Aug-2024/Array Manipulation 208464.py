# Problem: Array Manipulation - https://www.hackerrank.com/challenges/crush/problem


def arrayManipulation(n, queries):
    # Write your code here
    arr = [0] * (n + 1)
    
    for a, b, k in queries:
        arr[a] += k
        if b + 1 <= n:
            arr[b + 1] -= k
    
    max_value = 0
    current_value = 0
    for i in range(1, n + 1):
        current_value += arr[i]
        if current_value > max_value:
            max_value = current_value
    
    return max_value