# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            count_ones = bin(i).count('1')
            res.append(count_ones)

        return res