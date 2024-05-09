# Problem: First Bad Version - https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n
        
        while left < right:
            mid = (left + right) // 2
            version = isBadVersion(mid)
            if version == False:
                left = mid + 1
            else:
                right = mid
        
        return left
