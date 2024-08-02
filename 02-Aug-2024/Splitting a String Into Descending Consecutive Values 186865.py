# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        def canSplit(start: int, prev_value: int) -> bool:
            if start == len(s):
                return True
            
            for end in range(start + 1, len(s) + 1):
                current_value = int(s[start:end])
                if current_value == prev_value - 1 and canSplit(end, current_value):
                    return True
            return False
        
        for i in range(1, len(s)):
            if canSplit(i, int(s[:i])):
                return True
        return False
