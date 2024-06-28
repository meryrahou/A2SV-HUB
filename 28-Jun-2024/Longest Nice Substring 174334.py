# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def is_nice(subs):
            char_set = set(subs)
            for char in char_set:
                if char.lower() not in char_set or char.upper() not in char_set:
                    return False
            return True

        def longest_nice_substring(subs):
            if len(subs) < 2:
                return ""
            if is_nice(subs):
                return subs
            char_set = set(subs)
            for i, char in enumerate(subs):
                if char.lower() not in char_set or char.upper() not in char_set:
                    left = longest_nice_substring(subs[:i])
                    right = longest_nice_substring(subs[i+1:])
                    return left if len(left) >= len(right) else right
            return ""
        
        return longest_nice_substring(s)
