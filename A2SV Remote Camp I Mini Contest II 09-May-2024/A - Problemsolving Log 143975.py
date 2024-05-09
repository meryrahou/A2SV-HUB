# Problem: A - Problemsolving Log - https://codeforces.com/gym/522997/problem/A

testcases = int(input())

for _ in range(testcases):
    n = int(input())
    string = input()
    log = [0] * 26
    solved = 0
    for c in string:
        log[ord(c) - ord('A')] += 1

    for i in range(26):
        if log[i] > i:
            solved += 1
    print(solved)
