# Problem:  King Escape - https://codeforces.com/problemset/problem/1033/A

n = int(input())


# alice
a_x, a_y = map(int, input().split())
# bob
b_x, b_y = map(int, input().split())
# target
c_x, c_y = map(int, input().split())


if (a_x < b_x and a_x > c_x) or (a_x > b_x and a_x < c_x) or (a_y < b_y and a_y > c_y) or (a_y > b_y and a_y < c_y):
    print("NO")
else:
    print("YES")
