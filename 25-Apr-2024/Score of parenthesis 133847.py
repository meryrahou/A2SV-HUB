# Problem: Score of parenthesis - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]  

        for char in s:
            if char == "(":
                stack.append(0)
            else:
                score = stack.pop()
                stack[-1] += max(2 * score, 1)

        return stack[0]