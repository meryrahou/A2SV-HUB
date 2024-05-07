# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for log in logs:
            if log != '../' and log != './':
                stack.append(log)
            elif log == '../' and stack:
                stack.pop()
        
        return len(stack)
        