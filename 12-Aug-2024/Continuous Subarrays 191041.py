# Problem: Continuous Subarrays - https://leetcode.com/problems/continuous-subarrays/

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        start = 0 

        min_queue = deque()
        max_queue = deque()
        
        res = 0
        for end in range(len(nums)):
            while min_queue and min_queue[-1] > nums[end]: 
                min_queue.pop()

            min_queue.append(nums[end])

            while max_queue and max_queue[-1] < nums[end]: 
                max_queue.pop()
            
            max_queue.append(nums[end])
        
            while max_queue[0] - min_queue[0] > 2:
                if nums[start] == max_queue[0] : 
                    max_queue.popleft()
                

                if nums[start] == min_queue[0]:
                    min_queue.popleft()
                
                start+=1

            res+= end-start+1   
    
        return res

