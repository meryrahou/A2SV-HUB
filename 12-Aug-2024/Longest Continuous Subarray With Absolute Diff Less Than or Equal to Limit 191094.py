# Problem: Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = deque()
        min_deque = deque()
        left = 0
        max_len = 0

        for right in range(len(nums)):
            while max_deque and nums[right] > nums[max_deque[-1]]:
                max_deque.pop()
            max_deque.append(right)
            
            while min_deque and nums[right] < nums[min_deque[-1]]:
                min_deque.pop()
            min_deque.append(right)

            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                left += 1
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()

            max_len = max(max_len, right - left + 1)

        return max_len
        min_queue.append(right)