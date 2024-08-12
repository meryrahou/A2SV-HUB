# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l,r = 0,len(citations)-1
        h = 0
        while l<=r:
            m = (r+l)//2
            if len(citations)-m > citations[m]:
                if citations[m] > h:
                    h = citations[m]
                l = m+1
            elif len(citations)-m < citations[m]:
                h = len(citations)-m
                r = m-1
            else:
                return citations[m]
        return h