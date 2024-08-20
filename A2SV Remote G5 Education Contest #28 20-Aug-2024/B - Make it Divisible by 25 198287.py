# Problem: B - Make it Divisible by 25 - https://codeforces.com/gym/543262/problem/B

testcases = int(input())    

for _ in range(testcases):
    string = input()
    number = str(string)
    length = len(string)

    ends = ["25", "50", "75", "00"]
    min_removals = float('inf')

    for end in ends:
        pos = 1
        found = False
        
        for i in range(length - 1, -1, -1):
            if string[i] == end[1]:
                pos = i
                found = True
                break
        
        if not found:
            continue
        
        for j in range(pos - 1, -1, -1):
            if string[j] == end[0]:
                min_removals = min(min_removals, (length - j - 2))
                break
    
    print(min_removals)