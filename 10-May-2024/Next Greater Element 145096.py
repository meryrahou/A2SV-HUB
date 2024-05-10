# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = deque()
        
        for num in reversed(nums2):
            while stack and num >= stack[-1]:
                stack.pop()
            if stack:
                next_greater[num] = stack[-1]
            stack.append(num)
        
        result = []
        for num in nums1:
            result.append(next_greater.get(num, -1))
        
        return result
