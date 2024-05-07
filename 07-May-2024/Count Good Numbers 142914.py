# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        evendig = (n+1) // 2
        odddig = n // 2
        mod = pow(10, 9) + 7
        return (pow(4, odddig, mod) * pow(5, evendig, mod)) % mod