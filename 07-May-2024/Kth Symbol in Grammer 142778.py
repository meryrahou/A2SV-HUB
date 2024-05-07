# Problem: Kth Symbol in Grammer - https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # finding the middle
        middle = pow( 2 , n-1 ) // 2
        #basecase
        if n == 1:
            return 0
        '''
        if k is in the first half of n, then you call the function with k
        else you XOR 1 with the emplacement of k in the first half
        why XOR 1 ?
         0 XOR 1 is 1
         1 XOR 1 is 0
        so the XOR gives the inverse of the number
        which garentees the inversion of the second half of the number
        '''
        p = 1
        if k <= middle :
            p = self.kthGrammar( n-1 , k )
        else:
            p = 1 ^ self.kthGrammar( n-1 , k - middle )
       
        return p