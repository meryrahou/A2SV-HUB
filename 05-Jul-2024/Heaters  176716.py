# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        def nearest(house, heaters):
            left, right = 0, len(heaters) - 1
            res = float('inf')
            while left <= right:
                mid = left + (right - left)//2
                res = min(res, abs(heaters[mid] - house))
                if house < heaters[mid]:
                    right = mid - 1
                elif house > heaters[mid]:
                    left = mid + 1
                else:
                    break
            return res

        heaters.sort()
        radius = 0
        for h in houses:
            radius = max(radius, nearest(h, heaters))
        return radius