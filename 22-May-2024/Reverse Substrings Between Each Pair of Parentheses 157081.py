# Problem: Reverse Substrings Between Each Pair of Parentheses - https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

class Solution:
    def reverseParentheses(self, s: str) -> str:
        def reverseSubstring(s: str) -> str:
            result = ""
            i = 0
            while i < len(s):
                if s[i] == '(':
                    count = 1
                    j = i + 1
                    while count > 0:
                        if s[j] == '(':
                            count += 1
                        elif s[j] == ')':
                            count -= 1
                        j += 1
                    result += reverseSubstring(s[i+1:j-1])[::-1]
                    i = j
                else:
                    result += s[i]
                    i += 1
            return result
        
        return reverseSubstring(s)

