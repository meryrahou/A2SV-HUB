# Problem: D - Team Composition: Programmers and Mathematicians - https://codeforces.com/gym/524150/problem/D


for t in range(int(input())):
    a, b = map(int, input().split())

    virtual_max_1 = (a + b)//4
    virtual_max_2 = min(a, b)
    print(min(virtual_max_1, virtual_max_2))