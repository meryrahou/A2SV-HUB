# Problem: Search Insert Position - https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, h = 0 , len(nums) -1
        while l <= h :
            m = l + (h - l) // 2
            if nums[m] > target:
                h = m - 1
            elif nums[m] == target:
                return m
            else:
                l = m + 1

        return l