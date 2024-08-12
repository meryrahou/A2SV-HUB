# Problem: E - Boxes Packing - https://codeforces.com/gym/500425/problem/E

n = int(input())
k = list(map(int, input().split()))

# second thought
logdict = {}
for i in range(n):
    if k[i] in logdict:
        logdict[k[i]] += 1
    else:
        logdict[k[i]] = 1
print(max(logdict.values()))



# initial submission : wrong on test case 4
#kset = set(k)
# print( n - len(kset) + 1)