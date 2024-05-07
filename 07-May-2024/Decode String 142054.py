# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        res = ''
        
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '[':
                stack.append((num, res))
                num = 0
                res = ''
            elif char == ']':
                prev_num, prev_res = stack.pop()
                res = prev_res + prev_num * res
            else:
                res += char

        return res