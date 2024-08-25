# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        nums_str = [str(num) for num in nums]

        n = len(nums_str)
        for i in range(n):
            for j in range(0, n - i - 1):
                if nums_str[j] + nums_str[j + 1] < nums_str[j + 1] + nums_str[j]:
                    nums_str[j], nums_str[j + 1] = nums_str[j + 1], nums_str[j]
        
        result = ''.join(nums_str)

        if result[0] == '0':
            return '0'
        else:
            return result
