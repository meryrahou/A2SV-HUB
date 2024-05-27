# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
    
        stack = []
        s3 = float('-inf')
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < s3:
                return True
            while stack and nums[i] > stack[-1]:
                s3 = stack.pop()
            stack.append(nums[i])
        
        return False
