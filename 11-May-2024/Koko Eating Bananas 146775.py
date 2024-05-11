# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        #count nb hours it takes koko to finish all piles and check if it's less than what's given : h
        def good(k):
            nbhours = 0
            for pile in piles:
                # ceil function tdir tdwir lel wihda b zyada
                nbhours += math.ceil(pile / k)
            return (nbhours <= h)
        
        low, high = 1 , max(piles)

        while low < high:
            mid = (high + low) // 2
            if good(mid):
                high = mid
            else:
                low = mid + 1

        return high