# Problem: Minimal string - https://codeforces.com/contest/797/problem/C

s = input().strip()

t = []
u = []

# Create 'mins' array which stores the minimum character from right to left
mins = [None] * len(s)
min_char = s[-1]

for i in range(len(s) - 1, -1, -1):
    min_char = min(min_char, s[i])
    mins[i] = min_char

idx = 0
while idx < len(s):
    if not t:
        t.append(s[idx])
        idx += 1
    else:
        if mins[idx] < t[-1]:
            t.append(s[idx])
            idx += 1
        else:
            u.append(t.pop())

# Add the rest of 't' to 'u'
u.extend(reversed(t))

# Output the result
print(''.join(u))
