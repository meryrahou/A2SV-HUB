# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
       
        def good(max_cap):
            print('mac' , max_cap)
            nbdays = 1
            cap = 0
            i = 0
            while i < len(weights):
                if cap + weights[i] <= max_cap:
                    cap += weights[i]
                else:
                    nbdays += 1
                    cap = weights[i]
                i += 1

            return (nbdays <= days)
        
        low, high = max(weights) , sum(weights)

        while low < high:
            mid = (low + high)//2
            if good(mid):
                high = mid
            else:
                low = mid + 1
                
        return high