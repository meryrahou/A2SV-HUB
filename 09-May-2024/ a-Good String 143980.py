# Problem:  a-Good String - https://codeforces.com/gym/522997/problem/C

testcases = int(input())
 
for _ in range(testcases):
    len = int(input())
    word = input()
    currentLetter = 'a'
 
    def findingnemo(word, currentLetter , len):
        ops = 0
        l = len // 2
        #base case
        if len == 1:
            if word[0] != currentLetter:
                return 1
            else:
                return 0
 
 
        half1 = l -  word[:l].count(currentLetter)
        half2 = l -  word[l:].count(currentLetter)
    
        return min( half1 + findingnemo(word[l:], chr(ord(currentLetter) + 1),l ) , half2 + findingnemo(word[:l], chr(ord(currentLetter) + 1),l))
 
    print(findingnemo(word, currentLetter, len))