# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        word = '0'
        for _ in range(n-1):
            w = ''
            
            for c in word:
                if c == '0': 
                    w += '1'
                else:
                    w += '0'
            word = word + '1' + w[::-1]
                
        return word[k-1]