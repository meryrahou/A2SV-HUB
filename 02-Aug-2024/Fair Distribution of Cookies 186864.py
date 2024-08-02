# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        def backtrack(index):
            if index == len(cookies):
                return max(distribution)
            
            answer = float('inf')
            for i in range(k):
                distribution[i] += cookies[index]
                answer = min(answer, backtrack(index + 1))
                distribution[i] -= cookies[index]
                
                if distribution[i] == 0:
                    break
            
            return answer
        
        distribution = [0] * k
        return backtrack(0)
