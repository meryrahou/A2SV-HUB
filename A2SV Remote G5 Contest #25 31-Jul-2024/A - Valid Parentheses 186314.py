# Problem: A - Valid Parentheses - https://codeforces.com/gym/537575/problem/A

list = list(map(str, input()))

stack = []
count = 0
for i in range(len(list)):
    if list[i] == "(":
        stack.append("(")
    
    elif list[i] == ")":
        if stack and stack[-1] == "(":
            stack.pop()
            count += 1

print(count*2)