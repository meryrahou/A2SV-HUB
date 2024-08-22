# Problem: House Robber II - https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        
        def rob_linear(nums):
            prev1, prev2 = 0, 0
            for num in nums:
                current = max(prev1, prev2 + num)
                prev2 = prev1
                prev1 = current
            return prev1
        
        max1 = rob_linear(nums[:-1])
        max2 = rob_linear(nums[1:])
        
        return max(max1, max2)        