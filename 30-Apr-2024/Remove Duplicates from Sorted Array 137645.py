# Problem: Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        slow_ptr = 0
        
        for fast_ptr in range(1, len(nums)):
            if nums[fast_ptr] != nums[slow_ptr]:
                slow_ptr += 1
                nums[slow_ptr] = nums[fast_ptr]
        
        return slow_ptr + 1
