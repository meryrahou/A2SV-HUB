# Problem: Validate Stack Sequences - https://leetcode.com/problems/validate-stack-sequences/

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = [pushed[0]]
        i = 1
        j = 0

        while i < len(pushed) and j < len(popped):
            
            if stack and popped[j] == stack[-1]:  
                j += 1
                stack.pop()
                continue 

            stack.append(pushed[i])
            i += 1

        while j < len(popped):
            if stack and stack[-1] == popped[j]:  
                stack.pop()
                j += 1
            else:
                return False

        return True