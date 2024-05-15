# Problem: Shortest Subarray with Sum at Least K - https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
     
        min_length = float('inf')
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        deque_idx = deque()

        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        for i in range(n + 1):
            while deque_idx and prefix_sum[i] - prefix_sum[deque_idx[0]] >= k:
                min_length = min(min_length, i - deque_idx.popleft())
            while deque_idx and prefix_sum[i] <= prefix_sum[deque_idx[-1]]:
                deque_idx.pop()
            deque_idx.append(i)

        return min_length if min_length != float('inf') else -1
