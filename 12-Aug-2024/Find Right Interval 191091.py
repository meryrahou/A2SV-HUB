# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

from bisect import bisect_left

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        arr = []
        n = len(intervals)
        for i in range(n):
            arr.append((intervals[i][0], i))
        arr.sort()
        
        ans = []
        for intv in intervals:

            low = bisect_left(arr,intv[1] , key=lambda x:x[0])

            if low >= n : 
                ans.append(-1)
            else : 
                ans.append(arr[low][1])
        
        return ans
