# Problem: K Items With the Maximum Sum - https://leetcode.com/problems/k-items-with-the-maximum-sum/

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        max_sum = 0

        ones_to_use = min(numOnes, k)
        max_sum += ones_to_use
        k -= ones_to_use

        zeros_to_use = min(numZeros, k)
        k -= zeros_to_use

        neg_ones_to_use = min(numNegOnes, k)
        max_sum -= neg_ones_to_use
        k -= neg_ones_to_use

        return max_sum