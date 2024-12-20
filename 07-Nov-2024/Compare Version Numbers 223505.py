# Problem: Compare Version Numbers - https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        
        max_l = max(len(v1), len(v2))
        
        for i in range(max_l):
            v1_p = v1[i] if i < len(v1) else 0
            v2_p = v2[i] if i < len(v2) else 0
            
            if v1_p > v2_p:
                return 1
            elif v1_p < v2_p:
                return -1
        
        return 0
