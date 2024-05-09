# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def helper(start, end):
            if start == end:
                return nums[start]
            return max(nums[start] - helper(start + 1, end), nums[end] - helper(start, end - 1))

        return helper(0, len(nums) - 1) >= 0