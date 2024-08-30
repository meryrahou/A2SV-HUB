# Problem: Palindromic Substrings - https://leetcode.com/problems/palindromic-substrings/description/

class Solution:
    def countSubstrings(self, s: str) -> int:
        def center_go(left, right):
            cpt = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                cpt += 1
                left -= 1
                right += 1
            return cpt
        
        total = 0
        for i in range(len(s)):
            total += center_go(i, i)
            total += center_go(i, i + 1)
        
        return total
