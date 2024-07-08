# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        
        def is_valid_part(s):
            return not (s.startswith("0") and len(s) > 1)
        
        for i in range(1, n):
            for j in range(i + 1, n):
                first, second = num[:i], num[i:j]
                
                if not is_valid_part(first) or not is_valid_part(second):
                    continue
                
                while j < n:
                    third = str(int(first) + int(second))
                    if not num.startswith(third, j):
                        break
                    
                    j += len(third)
                    first, second = second, third
                
                if j == n:
                    return True
        
        return False
