# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
    
        bitmasks = [0] * n
    
        for i in range(n):
            bitmask = 0
            for char in words[i]:
                bitmask |= (1 << (ord(char) - ord('a')))
            bitmasks[i] = bitmask

        max_product = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                if bitmasks[i] & bitmasks[j] == 0:
                    product = len(words[i]) * len(words[j])
                    max_product = max(max_product, product)
        
        return max_product
